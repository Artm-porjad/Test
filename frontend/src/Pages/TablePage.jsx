import React, {useEffect, useState} from "react";
import Button from "react-bootstrap/Button";
import { Form } from "react-bootstrap";
import Modal from "../components/Modal";
import TableData from "../components/Table";
import Dropdown from "../components/dropDown";
import { ExportCSV } from "../components/ExportCSV";


const data = [
  [
    "Рег. номер МКС в СЭД",
    "Дата поступления в МКС",
    "Название документа",
    "В дополнение к или взамен (предыстория документа)",
    "ФОИВ",
    "Куратор АПРФ",
    "Направление",
    "Фед. Проект / ГИС",
    "Тип документа",
    "Решение по документу",
    "Текущий статус",
    "Финансовая оценка, тыс. руб.",
    "Экспертная оценка, тыс. руб.",
    "Реквизиты ответа в ведомство",
    "Дата ответа в ведомство",
  ],
  [
    [],
    [],
    [],
    [],
    [
      "Федеральный фонд обязательного медицинского страхования",
      "МВД России",
      "Рослесхоз",
    ],
    ["Иванов", "Курочкин"],
    ["1", "2"],
    ["1", "2"],
    ["1", "2"],
    [],
    [],
    [],
    [],
    [],
    [],
  ],
  [
    "111",
    "11.01.22",
    "ТЗ в рамках согласования Распоряжения ",
    "-",
    "Федеральный фонд обязательного медицинского страхования",
    "Иванов",
    "Здравоохранение",
    "ГИС ГМП",
    "ТЗ",
    "Согласовано с учетом замечаний",
    "Исполнено",
    "50",
    "100",
    "333",
    "07.04.2022",
  ],
  [
    "222",
    "11.01.22",
    "ТЗ в рамках согласования Распоряжения ",
    "-",
    "Федеральный фонд обязательного медицинского страхования",
    "Иванов",
    "Здравоохранение",
    "ГИС ГМП",
    "ТЗ",
    "Согласовано с учетом замечаний",
    "Исполнено",
    "50",
    "100",
    "333",
    "07.04.2022",
  ],
  [
    "33",
    "11.01.22",
    "ТЗ в рамках согласования Распоряжения ",
    "-",
    "Федеральный фонд обязательного медицинского страхования",
    "Иванов",
    "Здравоохранение",
    "ГИС ГМП",
    "ТЗ",
    "Согласовано с учетом замечаний",
    "Исполнено",
    "50",
    "100",
    "333",
    "07.04.2022",
  ],
];

const typeArr = [
  "text",
  "text",
  "text",
  "text",
  "text",
  "text",
  "text",
  "text",
  "number",
  "text",
  "date",
  "text",
  "text",
  "text",
  "text",
  "text",
  "number",
  "date",
  "date",
  "text",
  "text",
  "text",
  "date",
];

const TablePage = () => {
  // Первоначальные данные



  const [contentFromBase, setContentFromBase] = useState(data);
  // Массив выпадающих списков
  const [dropdownList, setDropdownList] = useState(data[1]);
  const content2 = JSON.parse(JSON.stringify(contentFromBase));
  // Состояние модального окна
  const [modal, setModal] = useState(false);
  const [modalRow, setModalRow] = useState([]);
  const [modalRowIndex, setModalRowIndex] = useState(0);
  // Заголовки столбцов
  const title = contentFromBase[0];

  const getContent = async (url) => {
    const response = await fetch(url);
    return await response.json();
  };

  const onSubmit = (event) => {
    setContentFromBase(content2);
    console.log(content2)
    setDropdownList(content2[1])
    const data = new FormData();
    data.append("data", JSON.stringify(content2));
    fetch("/api/test1", {
      method: "POST",
      body: data,
    }).finally(() => console.log(123));
    event.preventDefault();
  };
  const onClick = (event) =>{
    const a = JSON.parse(JSON.stringify(contentFromBase));
    a[a.length] = [['-'],['-'],['-'],['-'],['-'],['-'],['-'],['-'],['-'],['-'],['-'],['-'],['-'],['-'],['-']]
    setContentFromBase(a)
  }
  useEffect(() => {
    getContent('/api/test').then((data) => {
      console.log(data)
      setContentFromBase(data);
      setDropdownList(data[1]);
    });
  }, []);


  const fileName = "Форма списка";

  return (
    <div className="App">
      <div>
        <Button
            style={{ margin: "1% 0 1% 87%"}}
            onClick={onClick}
        >
          Добавить новую экспертизу
        </Button>

        {modal && (
          <Modal onClose={() => setModal(false)} title="Форма карточки">
            <Form style={{display: 'flex', flexFlow: 'column wrap'}} onSubmit={onSubmit}>
              {title.map((nameColumn, key) => {
                return (
                  <Dropdown
                    title={nameColumn}
                    dropdownList = {dropdownList[key]}
                    data={modalRow[key]}
                    index_column={key}
                    index_row={modalRowIndex + 1}
                    key={key}
                    content2={content2}
                    content={contentFromBase}
                    typeArr={typeArr}
                  />
                );
              })}

              <Button
                style={{ marginLeft: "87%" }}
                variant="primary"
                type="submit"
              >
                Сохранить изменения
              </Button>
            </Form>
          </Modal>
        )}
      </div>
      <TableData
        typeArr={typeArr}
        title={title}
        data={contentFromBase.slice(2)}
        setModal={setModal}
        setModalRow={setModalRow}
        setModalRowIndex={setModalRowIndex}
      />

      <ExportCSV csvData={contentFromBase} fileName={fileName} />
    </div>
  );
};

export default TablePage;
