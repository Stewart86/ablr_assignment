import React from 'react'

export const Field = ({ fieldName, value }) => {
    return (
        <div className='flex-row w-full mb-3 mt-3'>
            <div className='text-gray-400'>
                {fieldName}
            </div>
            <div className='font-semibold'>
                {value}
            </div>
        </div>
    )
}
