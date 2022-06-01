import Image from 'next/image'
import Link from 'next/link'
import React from 'react'
import openseaLogo from '../assets/opensea.png'
import { AiOutlineSearch } from 'react-icons/ai'
import { CgProfile } from 'react-icons/cg'
import { MdOutlineAccountBalanceWallet } from 'react-icons/md'
import toast, { Toaster } from 'react-hot-toast'
const style = {
  wrapper: `bg-[#04111d] w-screen px-[1.2rem] py-[0.8rem] flex `,
  logoContainer: `flex items-center cursor-pointer`,
  logoText: ` ml-[0.8rem] text-white font-semibold text-2xl`,
  searchBar: `flex flex-1 mx-[0.8rem] w-max-[520px] items-center bg-[#363840] rounded-[0.8rem] hover:bg-[#4c505c]`,
  searchIcon: `text-[#8a939b] mx-3 font-bold text-lg`,
  searchInput: `h-[2.6rem] w-full border-0 bg-transparent outline-0 ring-0 px-2 pl-0 text-[#e6e8eb] placeholder:text-[#8a939b]`,
  headerItems: ` flex items-center justify-end`,
  headerItem: `text-white px-4 font-bold text-[#c8cacd] hover:text-white cursor-pointer`,
  headerIcon: `text-[#8a939b] text-3xl font-black px-4 hover:text-white cursor-pointer`,
}

const Header = () => {
  return (
    <div className={style.wrapper}>
      <Toaster position="top-center" reverseOrder={false} />
      <Link href="/">
        <div className={style.logoContainer}>
          <Image src={openseaLogo} height={40} width={40} />
          <div className={style.logoText}>Columbia Fintech SBT</div>
        </div>
      </Link>
      <div className={style.searchBar}>
        <div className={style.searchIcon}>
          <AiOutlineSearch />
        </div>
        <input
          className={style.searchInput}
          placeholder="Bold of you to think I implemented search functionality"
        />
      </div>
      <div className={style.headerItems}>
        <Link href="/collections/0xb78f127b5C48d9351BB7da3A6D6A8cF6a948b23B">
          <div className={style.headerItem}> The Collection </div>
        </Link>
        <button onClick={() => toast.success(`This is limited time so this \nsite will self destruct in\n${
          //days, hours and minutes until june 1st 2022
          parseInt((new Date(2022, 5, 2) - new Date()) / (1000 * 60 * 60 * 24))
        } days and ${
          parseInt((new Date(2022, 5, 2).getTime() - new Date().getTime()) / 1000 / 60 / 60%24)
        } hours and ${
          parseInt((new Date(2022, 5, 2).getTime() - new Date().getTime()) / 1000 / 60 % 60)
        } minutes`, {duration:4000})}>
        <div className={style.headerItem}> SelfDestruct </div>
        </button>
        {/* <div className={style.headerItem}> Resources </div>
        <div className={style.headerItem}> Create </div> */}
        {/* <div className={style.headerIcon}>
          <CgProfile />
        </div> */}
        <div className={style.headerIcon}>
          <MdOutlineAccountBalanceWallet />         
        </div>
      </div>
    </div>
  )
}

export default Header
