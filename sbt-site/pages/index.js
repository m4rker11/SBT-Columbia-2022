import Head from 'next/head'
import Header from '../components/Header'
import Hero from '../components/Hero'
import { useWeb3 } from '@3rdweb/hooks'
import { useEffect } from 'react'

import toast, { Toaster } from 'react-hot-toast'
import sanityClient from '@sanity/client'
const client = sanityClient({
  projectId: '56wynask',
  dataset: 'production',
  apiVersion: '2021-03-25',
  token:
    'skDhgc6KBzOJCn9zEzleh2KFEboQztHUkJXb6z52suRnzZyMLZ3JLMAMNbK8yeIpzaXaNQ9tUMXEuWhVlK9Sdu06Hfh0pMingV8HV61cojpBphnt7wl9cx2ndxtGywYIBhVgu0K1OMYA0KzacZdc5JvF2rkKPjPpWsyyQh2GQnpOtTIoOYEQ',  
  useCdn: false,
})
const style = {
  wrapper: ``,
  walletConnectWrapper: `flex flex-col justify-center items-center h-screen w-screen bg-[#3b3d42] `,
  button: `border border-[#282b2f] bg-[#2081e2] p-[0.8rem] text-xl font-semibold rounded-lg cursor-pointer text-black`,
  details: `text-lg text-center text=[#282b2f] font-semibold mt-4`,
}

export default function Home() {
  const { address, connectWallet } = useWeb3()
  console.log(address)

  const welcomeUser = (userName, toastHandler = toast) => {
    toastHandler.success(
      `Welcome back${userName !== 'Unnamed' ? ` ${userName}` : ''}!`,
      {
        style: {
          background: '#04111d',
          color: '#fff',
        },
      }
    )
  }

  useEffect(() => {
    if (!address) return
    ;(async () => {
      const userDoc = {
        _type: 'users',
        _id: address,
        userName: 'Unnamed',
        walletAddress: address,
      }

      const result = await client.createIfNotExists(userDoc)

      welcomeUser(result.userName)
    })()
  }, [address])

  return (
    <div className={style.wrapper}>
      <Toaster position="top-center" reverseOrder={false} />
      {address ? (
        <>
          <Header />
          <Hero />
        </>
      ) : (
        <div className={style.walletConnectWrapper}>
          <button
            className={style.button}
            onClick={
              async () =>{try { await window.ethereum.request({ method: 'wallet_addEthereumChain',
                params: [{
                            chainId: '0x13881',
                            chainName: 'Mumbai Testnet',
                            nativeCurrency: {
                                name: 'MATIC',
                                symbol: 'MATIC',
                                decimals: 18
                            },
                            rpcUrls: [' https://rpc-mumbai.maticvigil.com'],
                            blockExplorerUrls: ['https://polygonscan.com/']
                        }]});
              } catch (e) {
                toast.error(
                  `Please install MetaMask and try again.`,
                  {})
              }


              }}
          >
            Add Mumbai
          </button>
          
          <div className={style.details}>
            OR
          </div>
          <div className={style.details}>
          </div>
          <button
            className={style.button}
            onClick={() => connectWallet('injected')}
          >
            Connect Wallet
          </button>
          <div className={style.details}>
            You need Chrome to be
            <br /> able to run this app.
          </div>
        </div>
      )}
    </div>
  )
}
