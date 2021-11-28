import { useState, useEffect } from "react"
import { ContactCard } from "../components/ContactCard"
import { PersonalCard } from "../components/PersonalCard"
import { IncomeCard } from "../components/IncomeCard"
import { OthersCard } from "../components/OthersCard"
import { useSearchParams, useNavigate } from "react-router-dom"



// to get data on load from backend
const Details = ({ infoToDisplay, data }) => {
  switch (infoToDisplay) {
    case 0:
      return <ContactCard data={data} />
    case 1:
      return <PersonalCard data={data} />
    case 2:
      return <IncomeCard data={data} />
    case 3:
      return <OthersCard data={data} />
    default:
      break;
  }
}

export default function Callback() {
  const navigate = useNavigate()
  const [infoToDisplay, setInfoToDisplay] = useState(0)
  const [data, setData] = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(false)
  const [searchParams] = useSearchParams()
  useEffect(() => {
    let mounted = true
    const getPerson = async () => {
      const response = await fetch(
        "http://localhost:3001/api/myinfo/retrieve/",
        {
          method: "POST",
          body: JSON.stringify({
            "code": searchParams.get("code")
          })
        }
      )
      if (mounted && response.status >= 200 && response.status <= 299) {
        const api_data = await response.json()
        setData(api_data)
        setLoading(false)
      } else if (response.status === 400 || response.status === 500) {
        setError(true)
      }
    }
    getPerson()
    return () => {
      mounted = false
    }
  }, [searchParams])

  if (error) {
    return <>Something when wrong, please try again <a href="/">here</a>.</>
  }

  return loading ? (<div className="mt-32">loading...</div>) : (
    <>
      <div
        className='flex flex-col sm:w-full lg:w-3/4 2xl:w-2/3 h-full bg-gray-200 overflow-hidden'
        style={{
          boxShadow:
            "0px 2px 3px 1px rgba(0,0,0,0.3),0px 2px 10px 4px rgba(0,0,0,0.3)"
        }}>
        <div className="flex-row bg-white">
          <div className="mt-11 ml-11 mb-5 text-xl">MyInfo</div>
        </div>
        <div className="flex flex-row w-full h-full">
          <div className="flex-col border w-36 h-full">
            {["Contact Info", "Personal Info", "Income Info", "Others"].map((item, index) => (
              <div className="flex flex-row bg-gray-200 h-10 text-sm justify-center items-center border-b w-full cursor-pointer hover:bg-white" key={index} onClick={() => setInfoToDisplay(index)}>
                {item}
              </div>
            )
            )}
          </div>
          <div className="flex flex-col bg-white w-full">
            <Details infoToDisplay={infoToDisplay} data={data} />
            <div className="border rounded cursor-pointer text-center bg-red-700 hover:bg-red-400 text-white w-36 m-2 p-1" onClick={() => navigate("/")}>Continue</div>
          </div>
        </div>
      </div>
    </>
  )
}
