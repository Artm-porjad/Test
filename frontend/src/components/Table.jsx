import Table from "react-bootstrap/Table";

const TableData = ({ typeArr, title, data, setModal, setModalRow, setModalRowIndex }) => {

    return (
        <>
            <Table striped bordered hover variant="light" size="sm">
                <thead className="table-primary text-center align-text-top">
                    <tr>
                        {title.map((nameColumn, key) => {
                            return <th key={key}>{nameColumn}</th>;
                        })}
                    </tr>
                </thead>
                <tbody className="text-center">
                    {data.map((row, key) => {
                        return(
                            <tr onClick={() => {
                                setModal(true);
                                setModalRow(row);
                                setModalRowIndex(key);
                            }} key={key}>
                                {row.map((nameColumn2, key)=>{
                                    return <td key={key}>{nameColumn2}</td>
                                    // (typeArr[key]=='date' ? (return <td key={key}>{nameColumn2.slice(8, 10)+'.'+nameColumn2.slice(5,7)+'.'+nameColumn2.slice(0,4)}</td>) : (return <td key={key}>{nameColumn2}</td>);
                            })}
                            </tr>
                        );
                    })}
                </tbody>
            </Table>
        </>
    );
};

export default TableData;
