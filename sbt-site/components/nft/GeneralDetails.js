const style = {
  wrapper: `flex`,
  infoContainer: `h-36 flex flex-col flex-1 justify-between mb-6`,
  accent: `text-[#2081e2]`,
  nftTitle: `text-3xl font-extrabold`,
  otherInfo: `flex`,
  ownedBy: `text-[#8a939b] mr-4`,
  likes: `flex items-center text-[#8a939b]`,
  likeIcon: `mr-1`,
  description: `text-lg text-[#8a939b]`,
  actionButtonsContainer: `w-44`,
  ctaContainer: `flex`,
  accentedButton: ` relative text-lg font-semibold px-8 py-2 bg-[#2181e2] rounded-lg mr-5 text-white hover:bg-[#42a0ff] cursor-pointer`,
  // actionButtons: `flex container justify-between text-[1.4rem] border-2 rounded-lg`,
  // actionButton: `my-2`,
  divider: `border-r-2`,
}


const GeneralDetails = ({ selectedNft }) => {

  return (
    <div className={style.wrapper}>
      <div className={style.infoContainer}>
        <div className={style.accent}>Columbia Fintech and BlockChain SBT</div>
        <div className={style.nftTitle}>{selectedNft?.name}</div>
        <div className={style.description}>{selectedNft?.description}</div>
        <div className={style.otherInfo}>
          <div className={style.ctaContainer}>
          </div>
          <div className={style.ownedBy}>
            Owned by <span className={style.accent}>Team 4</span>
          </div>
        </div>
      </div> 
    </div>
  )
}

export default GeneralDetails
