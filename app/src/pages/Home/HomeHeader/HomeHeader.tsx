import { FilePicker } from "@capawesome/capacitor-file-picker";
import { Search2Icon } from "@chakra-ui/icons";
import {
  Container,
  Center,
  ButtonGroup,
  WrapItem,
  Button,
  Icon,
} from "@chakra-ui/react";
import { BoundFunction } from "@testing-library/react";
import { useCallback, useRef, useState } from "react";
import zlib from "node:zlib";
import fs from "fs";
import unzipper from "unzipper";
import JSZip from "jszip";
export default function HomeHeader({ setXml }: { setXml: any }) {
  const [xmlFile, setXmlFile] = useState<any>("");
  const [AudioFile, setAudioFile] = useState<string | null>("");
  const xmlFileElement = useRef<HTMLInputElement | null>(null);
  const audioFileElement = useRef<HTMLInputElement | null>(null);

  const handleXmlFileChange = (event: any) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();

      const isMxl = file.name.endsWith(".mxl");
      console.log(file)
      reader.onload = (e) => {
        const value = 
          isMxl ?
            String.fromCharCode.apply(null, new Uint8Array(reader.result as ArrayBuffer) as any) :
            reader.result as string;
        
        setXml(value);
      };
      if (isMxl) {
        reader.readAsArrayBuffer(file);
      } else {
        reader.readAsText(file);
      }
      // setXml(file);
    }
    console.log("file", file);
  };

  const handleAudioFileChange = (event: any) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        setAudioFile(e.target!.result as string);
      };
      reader.readAsText(file);
    }
    console.log("file", file);
  };

  return (
    <Container>
      <Center>
        <ButtonGroup>
          <WrapItem>
            <Button
              onClick={() => {
                if (xmlFileElement.current) {
                  xmlFileElement.current.click();
                }
              }}
              colorScheme="cyan"
              marginTop={5}
              // onChange={handleFileChange}
            >
              <input
                type="file"
                onChange={handleXmlFileChange}
                style={{ display: "none" }}
                id="inputXml"
                accept=".xml"
                ref={xmlFileElement}
              />
              Load Sheet
            </Button>
          </WrapItem>
          <WrapItem>
            <Button
              onClick={() => {
                if (audioFileElement.current) {
                  audioFileElement.current.click();
                }
              }}
              colorScheme="cyan"
              marginTop={5}
            >
              <input
                type="file"
                onChange={handleAudioFileChange}
                style={{ display: "none" }}
                id="inputAudio"
                accept="audio/*"
                ref={audioFileElement}
              />
              Load Recording
            </Button>
          </WrapItem>
          <WrapItem>
            <Button colorScheme="cyan" marginTop={5}>
              <Icon as={Search2Icon}></Icon>
            </Button>
          </WrapItem>
        </ButtonGroup>
      </Center>
    </Container>
  );
}

// //? XML FILE
// const pickXml = async () => {
//   try {
//     const result = await FilePicker.pickFiles({
//       types: [".mxl"],
//     });
//   } catch (error) {}
// };

// //? AUDIO FILE
// const pickAudio = async () => {
//   try {
//     const result = await FilePicker.pickFiles({
//       types: ["audio/*"],
//     });
//   } catch (error) {}
// };
