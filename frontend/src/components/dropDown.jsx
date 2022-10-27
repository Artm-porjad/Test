import React, {useState} from "react";
import Dropdown from "react-bootstrap/Dropdown";
import DropdownButton from "react-bootstrap/DropdownButton";
import Form from "react-bootstrap/Form";
import InputGroup from "react-bootstrap/InputGroup";
import 'date-input-polyfill';

const DropDown = ({title, data, index_column, index_row, content2, content, dropValue, typeArr}) => {
    const [result, setResult] = useState(data);
    const handlerSelect= (e)=>{
        setResult(e);
    }

    content2[index_row + 1][index_column] = result
    const onChange = (e)=>{
        setResult(e.currentTarget.value);

    }
    return (
        <>
            <Form.Label>{title}</Form.Label>
            <InputGroup className="mb-3">
                <Form.Control
                    name="text"
                    type={typeArr[index_column]}
                    value={result}
                    defaultValue={result}
                    onChange={onChange}
                />
                {dropValue.length !== 0 && <DropdownButton
                    onSelect={handlerSelect}
                    variant="outline-secondary"
                    title={''}
                    id="input-group-dropdown-1"
                >
                    {dropValue.map((value, key) => {
                        return (<Dropdown.Item key={key} eventKey={value}>{value}</Dropdown.Item>)
                    })
                    }
                    <Dropdown.Divider/>
                </DropdownButton>}



                {/*{typeArr[index_column] === 'date'*/}
                {/*    ?*/}
                {/*    <Form.Control*/}
                {/*    data-date-format="dd/mm/yyyy"*/}
                {/*    name="text"*/}
                {/*    type={typeArr[index_column]}*/}
                {/*    value={result}*/}
                {/*    defaultValue={result}*/}
                {/*    onChange={onChange}*/}

                {/*/> : <Form.Control*/}
                {/*        name="text"*/}
                {/*        type={typeArr[index_column]}*/}
                {/*        value={result}*/}
                {/*        defaultValue={result}*/}
                {/*        onChange={onChange}*/}
                {/*    />}*/}


            </InputGroup>
        </>
    );
}


export default DropDown;
