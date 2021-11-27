import { Field } from "./Field"
import { FieldTitle } from "./FieldTitle"

export const ContactCard = ({ data }) => {
    return (
        <div className="flex flex-col ml-9">
            <FieldTitle title="Contact Info" />
            <Field fieldName="Mobile Number" value={data.mobileno.nbr.value} />
            <Field fieldName="Email" value={data.email.value} />
            <FieldTitle title="Registered Address" />
            <Field fieldName="Block Number" value={data.regadd.block.value} />
            <Field fieldName="Street Name" value={data.regadd.street.value} />
            <Field fieldName="Building Name" value={data.regadd.building.value} />
            <Field fieldName="Floor & Unit No" value={`#${data.regadd.floor.value}-${data.regadd.unit.value}`} />
            <Field fieldName="Postal Code" value={data.regadd.postal.value} />
            <Field fieldName="Type of Housing" value={data.hdbtype.desc} />
        </div>
    )
}
