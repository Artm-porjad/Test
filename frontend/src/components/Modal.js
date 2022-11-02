import React from "react";
import CloseButton from "react-bootstrap/CloseButton";

const Modal = ({ title, onClose, children }) => {
    return (
        <div id="modal">
            <>
                <div
                    className="fixed bg-black/50 top-0 right-0 left-0 bottom-0"
                    onClick={onClose}
                />

                <div className=" w-[1300px] h-[295%] p-5 rounded bg-white absolute top-2 left-1/2 -translate-x-1/2">
                    <div id="closeBtn">
                        <CloseButton onClick={onClose} />
                    </div>
                    <h1 className="text-2 text-center mb-2">{title}</h1>
                    {children}
                </div>
            </>
        </div>
    );
};

export default Modal;