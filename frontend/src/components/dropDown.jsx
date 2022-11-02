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
    const handlerSelect= (e)=>{
        setResult(e.target.value);
        setTitleDropDown(e)
        console.log('hi')
    }

    content2[index_row + 1][index_column] = result
    const onChange = (e)=>{
        setResult(e.currentTarget.value);
    }

    const inputId = typeIndex === "date" || typeIndex === "number" || index_column === 0 ? "input-date-number" : ''

    return (
        <div style={{paddingTop: "17px"}}>
            <Form.Label>{title}</Form.Label>
            <InputGroup >
                {dropValue.length === 0 && <Form.Control
                    disabled={false}
                    id={inputId}
                    name="text"
                    type={typeArr[index_column]}
                    value={result}
                    defaultValue={result}
                    onChange={onChange}
                />}

                {/*{dropValue.length !== 0 && <>*/}
                {/*    <Form.Control id="input-group-dropdown-1" placeholder={result} disabled={true}/>*/}
                {/*    <DropdownButton*/}
                {/*        title=""*/}
                {/*        onSelect={handlerSelect}*/}
                {/*        variant="outline-secondary"*/}
                {/*        onChange={() => setResult(titleDropDown)}*/}
                {/*    >*/}
                {/*        {dropValue.map((value, key) => {*/}
                {/*            return (<Dropdown.Item key={key} eventKey={value}>{value}</Dropdown.Item>)*/}
                {/*        })*/}
                {/*        }*/}
                {/*        <Dropdown.Divider/>*/}
                {/*    </DropdownButton>*/}
                {/*</>}*/}

                {dropValue.length !== 0 &&
                    <Form.Select
                        aria-label="Default select example"
                        onChange={handlerSelect}
                        // onChange={() => setResult(titleDropDown)}
                    >
                        <option>

                        </option>
                        {dropValue.map((value, key) => {
                            return (<option key={key}>{value}</option> )
                        })}
                    </Form.Select>}
            </InputGroup>
        </div>
    );
}


export default DropDown;

{/*{dropValue.length !== 0 && <DropdownButton*/}
{/*    aria-disabled={true}*/}
{/*    onSelect={handlerSelect}*/}
{/*    variant="outline-secondary"*/}
{/*    title={titleDropDown}*/}
{/*    id="input-group-dropdown-1"*/}
{/*    onChange={() => setResult(titleDropDown)}*/}
{/*>*/}
{/*    {dropValue.map((value, key) => {*/}
{/*        return (<Dropdown.Item key={key} eventKey={value}>{value}</Dropdown.Item>)*/}
{/*    })*/}
{/*    }*/}
{/*    <Dropdown.Divider/>*/}
{/*</DropdownButton>}*/}
