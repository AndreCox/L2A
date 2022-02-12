import React from 'react';

// returns a button with the given text you can add more components to this folder
function Button(props: {
  text: string;
  onClick?: () => void;
  className?: string;
}) {
  return (
    <button
      type="button"
      className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-xl transition-all shadow shadow-blue-800 hover:shadow-black hover:scale-105"
      onClick={props.onClick}
    >
      {props.text}
    </button>
  );
}

export default Button;
