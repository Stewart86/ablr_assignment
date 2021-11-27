import { Field } from "./Field"

export const OthersCard = ({ data }) => {
    return (
        <div className="flex flex-col ml-9">
            <Field fieldName="Employment Sector" value={data.employmentsector.value} />
            <Field fieldName="Marital Status" value={data.marital.desc} />
            <Field fieldName="Education Level" value={data.edulevel.desc} />
            <Field fieldName="Alias Name" value={data.aliasname.value} />
            <Field fieldName="Married Name" value={data.marriedname.value} />
            <Field fieldName="Married Name" value={data.marriedname.value} />
            <Field fieldName="Pass Type" value={data.passtype.value} />
        </div>
    )
}
