import { useEffect, useState } from 'react'

import { HiTag } from 'react-icons/hi'
import { IoMdWallet } from 'react-icons/io'
import toast, { Toaster } from 'react-hot-toast'
import { useRouter } from "next/router";
const style = {
  button: `mr-8 flex items-center py-2 px-12 rounded-lg cursor-pointer`,
  buttonIcon: `text-xl`,
  buttonText: `ml-2 text-lg font-semibold`,
}

const MakeOffer = ({ isListed, selectedNft, listings, marketPlaceModule }) => {
  const [selectedMarketNft, setSelectedMarketNft] = useState()
  const [enableButton, setEnableButton] = useState(false)
  // get nft id from url
  const nftId = useRouter().query.nftId
  console.log(nftId)
  selectedMarketNft
  useEffect(() => {
    if (!selectedMarketNft || !selectedNft) return

    setEnableButton(true)
  }, [selectedMarketNft, selectedNft])

  const confirmPurchase = (toastHandler = toast) =>
    toastHandler.success(`Claim recieved, due to the SBT being free, you are not guaranteed to recieve the horse you selected,
    The transaction is being signed externally and will go through by the end of the day.`, {
      style: {
        background: '#04111d',
        color: '#fff',
      },
    })
    

  const buyItem = async (
    listingId = nftId,
    quantityDesired = 1,
    module = marketPlaceModule
  ) => {

    

    // beginPurchase()
    console.log(listingId, quantityDesired, module)
    let address = window.ethereum.selectedAddress
    console.log(address)
    console.log(listingId, quantityDesired, module)
    // module.sdk._providerOrSigner._address = address]

    toast.promise(module.transfer(address, listingId, quantityDesired), {
      loading: '`Transaction is being signed, please wait...',
      success: 'Your SBT has been sent to your wallet, you can transfer it until the end of the day to the desired location',
      error: 'This SBT has already been claimed, please ick another one ~~HURRY~~',
    });
    // try {
    //   await module.transfer(address, listingId, quantityDesired)
    //   confirmPurchase()}
    // catch(e) {
    //   toast.error(`Transaction failed, please try again.`, {
    //     style: {
    //       background: '#04111d',
    //       color: '#fff',
    //     },
    //   })
    // }
    
    
    // await module
    //   .buyoutDirectListing({
    //     listingId: listingId,
    //     quantityDesired: quantityDesired,
    //   })
    //   .catch((error) => console.error(error))
    return true
  }

  return (
    <div className="flex h-20 w-full items-center rounded-lg border border-[#151c22] bg-[#303339] px-12">
      {/* <Toaster position="bottom-left" reverseOrder={false} /> */}
      {/* {isListed === 'true' ? ( */}
        <>
          <div
            onClick={() => {
              //get id from query string
              // let id = window.location.search.split('/')[4].split('?')[0]
              buyItem(nftId, 1, marketPlaceModule)
            }}
            className={`${style.button} bg-[#2081e2] hover:bg-[#42a0ff]`}
          >
           <IoMdWallet className={style.buttonIcon} />
            <div className={style.buttonText}>Claim</div>
            
          </div>
          Don't click twice
        </>
      {/* ) : (
        <div className={`${style.button} bg-[#2081e2] hover:bg-[#42a0ff]`}>
          <IoMdWallet className={style.buttonIcon} />
          <div className={style.buttonText}>List Item</div>
        </div>
      )} */}
    </div>
  )
}

export default MakeOffer
