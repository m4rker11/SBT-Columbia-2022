import Header from '../../components/Header'
import { useEffect, useMemo, useState } from 'react'
import { useWeb3 } from '@3rdweb/hooks'
// import { ThirdwebSDK } from '@3rdweb/sdk' //old

import { ThirdwebSDK } from '@thirdweb-dev/sdk'
import { useRouter } from 'next/router'
import NFTImage from '../../components/nft/NFTImage'
import GeneralDetails from '../../components/nft/GeneralDetails'
import ItemActivity from '../../components/nft/ItemActivity'
import Purchase from '../../components/nft/Purchase'

const style = {
  wrapper: `flex flex-col items-center container-lg text-[#e5e8eb]`,
  container: `container p-6`,
  topContent: `flex`,
  nftImgContainer: `flex-1 mr-4`,
  detailsContainer: `flex-[2] ml-4`,
}

const Nft = () => {
  const { provider } = useWeb3()
  const [selectedNft, setSelectedNft] = useState()
  const [listings, setListings] = useState([])
  const router = useRouter()

  const nftModule = useMemo(() => {
    if (!provider) return

    const sdk = ThirdwebSDK.fromPrivateKey("efad97be8131aa6e125f59094673e2c70c4c9260577ee70954493ccddccdd351",'mumbai',
      // provider.getSigner(),
      // 'https://polygon-mumbai.g.alchemy.com/v2/npmkfPpuARktsK4CJgwVB0jDs64oD_g6'
      
      {
        gassless: {
          openzeppelin: "https://api.defender.openzeppelin.com/autotasks/d8b7124e-6970-49b9-954c-940eabba3b5f/runs/webhook/17c82d22-5566-4016-add9-554ed81f8868/JTUL6EQFpencxCVcxTJgoa"
        }
      }
      )
    return sdk.getNFTCollection('0xfd58fD1C9aC97224931EB17B5c1ae4c0904DA43B')
  }, [provider])

  // get all NFTs in the collection
  useEffect(() => {
    if (!nftModule) return
    ;(async () => {
      const nfts = await nftModule.getAll()
      // console.log(router.query.nftId)
      const selectedNftItem = nfts[router.query.nftId]
      // const selectedNftItem = nfts.find((nft) => nft.id === router.query.nftId)
      console.log(selectedNftItem)
      setSelectedNft(selectedNftItem)
    })()
  }, [nftModule])
  // console.log(selectedNft.metadata.image)
  const marketPlaceModule = useMemo(() => {
    if (!provider) return

    const sdk = new ThirdwebSDK(
      // provider.getSigner(),
      // 'https://polygon-mumbai.g.alchemy.com/v2/npmkfPpuARktsK4CJgwVB0jDs64oD_g6',
      'mumbai',{
        gassless: {
          openzeppelin: {
            relayerUrl: "https://api.defender.openzeppelin.com/autotasks/d8b7124e-6970-49b9-954c-940eabba3b5f/runs/webhook/17c82d22-5566-4016-add9-554ed81f8868/JTUL6EQFpencxCVcxTJgoa",
          },
        }
      }
    )

    return sdk.getNFTCollection('0xfd58fD1C9aC97224931EB17B5c1ae4c0904DA43B')
    // return sdk.getMarketplace(
    //   '0xee0a517DA86E5E13b7BbcD36BB752D499C0eF06F'
    // )
  }, [provider])

  useEffect(() => {
    if (!marketPlaceModule) return
    ;(async () => {
      setListings(await marketPlaceModule.getAll())
    })()
  }, [marketPlaceModule])
  // console.log(listings)
  // selectedNft = selectedNftItem
  return (
    <div>
      <Header />
      <div className={style.wrapper}>
        <div className={style.container}>
          <div className={style.topContent}>
            <div className={style.nftImgContainer}>
              <NFTImage selectedNft={selectedNft} />
            </div>
            <div className={style.detailsContainer}>
              <GeneralDetails selectedNft={selectedNft} />
              <Purchase
                isListed={router.query.isListed}
                selectedNft={selectedNft}
                listings={listings}
                marketPlaceModule={nftModule}
              />
            </div>
          </div>
          <ItemActivity />
        </div>
      </div>
    </div>
  )
}

export default Nft
