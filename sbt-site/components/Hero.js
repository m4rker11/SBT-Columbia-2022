import Link from 'next/link'
import React from 'react'

const style = {
  wrapper: `relative`,
  container: `before:content-[''] before:bg-red-500 before:absolute before:top-0 before:left-0 before:right-0 before:bottom-0 before:bg-[url('https://roost.nbcuni.com/bin/viewasset.html/content/dam/Peacock/Landing-Pages/sports/horseracing/triplecrown/kentucky-derby-hero-d.jpg/_jcr_content/renditions/original.JPEG')] before:bg-cover before:bg-center before:opacity-45 before:blur`,
  contentWrapper: `flex h-screen relative justify-center flex-wrap items-center`,
  copyContainer: `w-1/2`,
  title: `relative text-white text-[46px] font-semibold`,
  description: `text-[#8a939b] container-[400px] text-2xl mt-[0.8rem] mb-[.5rem]`,
  ctaContainer: `flex`,
  accentedButton: ` relative text-lg font-semibold px-12 py-4 bg-[#2181e2] rounded-lg mr-5 text-white hover:bg-[#42a0ff] cursor-pointer`,
  button: ` relative text-lg font-semibold px-12 py-4 bg-[#363840] rounded-lg mr-5 text-[#e4e8ea] hover:bg-[#4c505c] cursor-pointer`,
  cardContainer: `rounded-[3rem] w-[500px] h-[50vh] relative`,
  infoContainer: `h-20 bg-[#313338] p-4 rounded-b-lg flex items-center text-white`,
  author: `flex flex-col justify-center ml-4`,
  name: ``,
  infoIcon: `flex justify-end items-center flex-1 text-[#8a939b] text-3xl font-bold`,
}

const Hero = () => {
  return (
    <div className={style.wrapper}>
      <div className={style.container}>
        <div className={style.contentWrapper}>
          <div className={style.copyContainer}>
            <div className={style.title}>
              CONGRATULATIONS! We did it. 
            </div>
            <div className={style.description}>
              We are now done with this bootcamp!
              <br/>And to commemorate the success 
              <br/>of our journey we got you a little
            </div>
            <div className={style.ctaContainer}>
            <Link href="/collections/0xb78f127b5C48d9351BB7da3A6D6A8cF6a948b23B">
              <button className={style.accentedButton}>Something</button>
            </Link>
            </div>
          </div>
          <div className={style.cardContainer}>
            <img
              className="rounded-t-lg"
              src="https://nypost.com/wp-content/uploads/sites/2/2022/05/Kentucky-Derby-Rich-Strike.jpg"
              alt=""
            />
            <div className={style.infoContainer}>
              <img
                className="h-[2.25rem] rounded-full"
                src="https://images.outbrainimg.com/transform/v3/eyJpdSI6Ijk5MmRjYzJjNzU4NWM5MzNjOTQ1MTE1MzNmYmMyOGEwNGEwZTNkZjRiYjcyY2M0OTc5MDkyYjM5ZDZhZTFiNzUiLCJ3Ijo0MCwiaCI6NDAsImQiOjIuMCwiY3MiOjAsImYiOjJ9.png"
                alt=""
              />
              <div className={style.author}>
                <div className={style.name}>Kentucky Derby</div>
                <a
                  className="text-[#1868b7]"
                  href="https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/2324922113504035910649522729980423429926362207300810036887725141691069366277"
                >
                  <Link href="https//nypost.com/2022/05/08/kentucky-derby-rich-strikes-win-from-overhead-video/">
                    NY-Post
                  </Link>
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Hero
