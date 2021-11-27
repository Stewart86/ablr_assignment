import { FieldTitle } from "./FieldTitle"
import { Field } from "./Field"

export const PersonalCard = ({data}) => {
    return (
        <div className="flex flex-col ml-9">
            <FieldTitle title="Personal Info" />
            <Field fieldName="NRIC/FIN" value={data.uinfin.value} />
            <Field fieldName="Principal Name" value={data.name.value} />
            <Field fieldName="Sex" value={data.sex.desc} />
            <Field fieldName="Date Of Birth" value={data.dob.value} />
            <Field fieldName="Country Of Birth" value={data.birthcountry.desc} />
            <Field fieldName="Residential Status" value={data.residentialstatus.desc} />
            <Field fieldName="Nationality" value={data.nationality.desc} />
            <Field fieldName="Race" value={data.race.desc} />
        </div>
    )
}
