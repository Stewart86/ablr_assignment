import React from 'react'

export default function Home() {

  const getInfoLogin = async () => {
    window.location.href = "api/myinfo/login/"
  }
  return (
    <>
      <div
        className='flex flex-col sm:w-full lg:w-3/4 2xl:w-2/3 h-full bg-gray-200 overflow-hidden'
        style={{
          boxShadow:
            "0px 2px 3px 1px rgba(0,0,0,0.3),0px 2px 10px 4px rgba(0,0,0,0.3)"
        }}>
        <div className="flex flex-row w-full h-full">
          <div className="flex flex-col justify-center items-center bg-white w-full">
            <div className='border rounded cursor-pointer text-center bg-red-700 hover:bg-red-400 text-white w-36 m-2 p-1' onClick={() => getInfoLogin()}>Retrieve MyInfo</div>
          </div>
        </div>
      </div>
    </>
  )
}
