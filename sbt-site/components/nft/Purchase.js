import { useEffect, useState } from 'react'

import { HiTag } from 'react-icons/hi'
import { IoMdWallet } from 'react-icons/io'
import toast, { Toaster } from 'react-hot-toast'

const style = {
  button: `mr-8 flex items-center py-2 px-12 rounded-lg cursor-pointer`,
  buttonIcon: `text-xl`,
  buttonText: `ml-2 text-lg font-semibold`,
}

const MakeOffer = ({ isListed, selectedNft, listings, marketPlaceModule }) => {
  const [selectedMarketNft, setSelectedMarketNft] = useState()
  const [enableButton, setEnableButton] = useState(false)

  useEffect(() => {
    if (!listings || isListed === 'false') return
    ;(async () => {
      setSelectedMarketNft(
        listings.find((marketNft) => marketNft.asset?.id === selectedNft.id)
      )
    })()
  }, [selectedNft, listings, isListed])

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
    listingId = selectedMarketNft.id,
    quantityDesired = 1,
    module = marketPlaceModule
  ) => {
    console.log(listingId, quantityDesired, module)
    let address = window.ethereum.selectedAddress
    console.log(address)
    console.log(listingId, quantityDesired, module)
    // module.sdk._providerOrSigner._address = address
    await module.transfer(address, listingId, quantityDesired)
    
    
    // await module
    //   .buyoutDirectListing({
    //     listingId: listingId,
    //     quantityDesired: quantityDesired,
    //   })
    //   .catch((error) => console.error(error))

    confirmPurchase()
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
              buyItem(1, 1, marketPlaceModule)
            }}
            className={`${style.button} bg-[#2081e2] hover:bg-[#42a0ff]`}
          >
            <IoMdWallet className={style.buttonIcon} />
            <div className={style.buttonText}>Buy Now</div>
          </div>
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
