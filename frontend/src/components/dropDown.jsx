import React, {useState} from "react";
import Dropdown from "react-bootstrap/Dropdown";
import DropdownButton from "react-bootstrap/DropdownButton";
import Form from "react-bootstrap/Form";
import InputGroup from "react-bootstrap/InputGroup";
import 'date-input-polyfill';

const DropDown = ({title, data, index_column, index_row, content2, dropValue, typeArr}) => {
    const [result, setResult] = useState(data);
    const [titleDropDown, setTitleDropDown] = useState(data);
    const [typeIndex, setTypeIndex] = useState(typeArr[index_column])
    const [dis, setDis] = useState(false)
    const handlerSelect= (e)=>{
        setResult(e);
        setTitleDropDown(e)
    }

    content2[index_row + 1][index_column] = result
    const onChange = (e)=>{
        setResult(e.currentTarget.value);
    }

    const inputId = typeIndex === "date" || typeIndex === "number" || index_column === 0? "input-date-number" : ''

    return (
        <>
            <Form.Label>{title}</Form.Label>
            <InputGroup className="mb-3">
                {dropValue.length === 0 && <Form.Control
                    disabled={false}
                    id={inputId}
                    name="text"
                    type={typeArr[index_column]}
                    value={result}
                    defaultValue={result}
                    onChange={onChange}
                />}
                {dropValue.length !== 0 && <DropdownButton
                    onSelect={handlerSelect}
                    variant="outline-secondary"
                    title={titleDropDown}
                    id="input-group-dropdown-1"
                    onChange={() => setResult(titleDropDown)}
                >
                    {dropValue.map((value, key) => {
                        return (<Dropdown.Item key={key} eventKey={value}>{value}</Dropdown.Item>)
                    })
                    }
                    <Dropdown.Divider/>
                </DropdownButton>}
            </InputGroup>
        </>
    );
}


export default DropDown;
