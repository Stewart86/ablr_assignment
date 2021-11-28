import { FieldTitle } from "./FieldTitle"
import { Field } from "./Field"

const boolConvert = (boolStr) => {
  switch (boolStr) {
    case "false":
      return "No"

    case "true":
      return "Yes"

    default:
      return "N/A"
  }
}

const convert = (value) => {
  const formatter = new Intl.NumberFormat('en-US', {
    minimumFractionDigits: 2
  })
  return formatter.format(value)
}

const NOALine = ({ title, values, heading = false, currency = false }) => (
  <div className={`flex flex-row ${heading && "font-bold"}`}>
    <div className="w-64">{title}</div>
    <div className="flex w-full">
      {values.map((item, i) => (
        <div key={i} className="flex-1 text-right">{currency ? convert(item) : item}</div>
      ))}
    </div>
  </div>
)

const NOAHistory = ({ history }) => {
  if (history === undefined) {
    return <div className="flex flex-col pr-10">No NOA</div>
  }
  return (<div className="flex flex-col pr-10">
    <NOALine title="Year Of Assessment" values={history.map((i) => i.yearofassessment.value)} heading />
    <NOALine title="Employment" values={history.map((i) => i.employment.value)} currency />
    <NOALine title="Trade" values={history.map((i) => i.trade.value)} currency />
    <NOALine title="Interest" values={history.map((i) => i.interest.value)} currency />
    <NOALine title="Rent" values={history.map((i) => i.rent.value)} currency />
    <NOALine title="Total Income" values={history.map((i) => i.amount.value)} heading currency />
    <NOALine title="Tax Clearance" values={history.map((i) => i.taxclearance.value)} heading />
  </div>
  )
}

const CPFAccount = ({ title, value }) => (
  <div className="flex flex-col pr-10">
    <div className={`flex flex-row`}>
      <div className="w-64">{title}</div>
      <div className="flex-1 text-right">{convert(value)}</div>
    </div>
  </div>
)


const CPFContribution = ({ history }) => {
  if (history === undefined) {
    return <div className="flex flex-col pr-10">No CPF Contribution</div>
  }
  return (
    <div className="flex flex-col pr-10 h-full">
      <div className="flex flex-row">
        <div className="w-1/4 font-semibold">
          For Month
        </div>
        <div className="w-1/4 font-semibold">
          Paid On
        </div>
        <div className="w-1/4 font-semibold">
          Amount (S$)
        </div>
        <div className="w-1/4 font-semibold">
          Employer
        </div>
      </div>
      {history && history.map((item, i) => (
        <div className="flex flex-row" key={i}>
          <div className="w-1/4">
            {item.month.value}
          </div>
          <div className="w-1/4">
            {item.date.value}
          </div>
          <div className="w-1/4">
            {convert(item.amount.value)}
          </div>
          <div className="w-1/4">
            {item.employer.value}
          </div>
        </div>
      ))}
    </div>
  )
}


export const IncomeCard = ({ data }) => {
  return (
    <div className="flex flex-col ml-9 overflow-auto h-5/6">
      <FieldTitle title="Notice of Assessment (History)" />
      <NOAHistory history={data.noahistory.noas} />
      <FieldTitle title="Other Income Information" />
      <Field fieldName="Ownership of Private Residential Property" value={boolConvert(data.ownerprivate.value)} />
      <FieldTitle title="CPF Account Balance" />
      <CPFAccount title="Ordinary Account (OA) (S$)" value={data.cpfbalances.oa.value} />
      <CPFAccount title="Special Account (SA) (S$)" value={data.cpfbalances.sa.value} />
      <CPFAccount title="Medisave Account (MA) (S$)" value={data.cpfbalances.ma.value} />
      <FieldTitle title="CPF Contribution History" />
      <CPFContribution history={data.cpfcontributions.history} />
    </div>
  )
}
