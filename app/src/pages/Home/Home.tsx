import {
  IonContent,
  IonHeader,
  IonPage,
  IonTitle,
  IonToolbar,
} from "@ionic/react";
// import ExploreContainer from "../components/ExploreContainer";
import ExploreContainer from "../../components/ExploreContainer";
import {
  Button,
  ButtonGroup,
  Center,
  Icon,
  Input,
  WrapItem,
  Text,
  VStack,
} from "@chakra-ui/react";
import { Grid, GridItem } from "@chakra-ui/react";
import { Container } from "@chakra-ui/react";
import "./Home.css";
import { Search2Icon } from "@chakra-ui/icons";
import { StaveNote, Vex } from "vexflow";
import { createElement, useEffect, useRef, useState } from "react";
import { Filesystem, Directory } from "@capacitor/filesystem";
import { FilePicker } from "@capawesome/capacitor-file-picker";
import { parseString } from "xml2js";
import { FaMusic } from "react-icons/fa";
import { Card, CardHeader, CardBody, CardFooter } from "@chakra-ui/react";
import { BsFileEarmarkMusic } from "react-icons/bs";
export default function Home() {
  const [xmlContent, setXmlContent] = useState<string | null>("");
  const pickXml = async () => {
    try {
      const result = await FilePicker.pickFiles({
        types: [".mxl"],
      });
    } catch (error) {}
  };
  const pickAudio = async () => {
    try {
      const result = await FilePicker.pickFiles({
        types: ["audio/*"],
      });
    } catch (error) {}
  };
  const handleFileChange = (event: any) => {
    const file = event.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (e) => {
        setXmlContent(e.target!.result as string);
      };
      reader.readAsText(file);
    }
    console.log("file", file);
  };

  const parseMusicXml = async (xml: any) => {
    return new Promise((resolve, reject) => {
      parseString(xml, (err, result) => {
        if (err) {
          reject(err);
        } else {
          resolve(result);
        }
      });
    });
  };

  const convertToVexFlowNotes = (musicXMLData: any) => {
    // Example function to convert a very simple MusicXML structure to VexFlow notes
    // This needs to be expanded based on actual MusicXML data
    const notes =
      musicXMLData["score-partwise"]["part"][0]["measure"][0]["note"];
    return notes.map((note: any) => {
      const pitch = note["pitch"][0];
      const step = pitch["step"][0];
      const octave = pitch["octave"][0];
      const duration = note["duration"][0];
      const noteName = `${step}/${octave}`;
      return new StaveNote({
        keys: [noteName],
        duration: duration,
      });
    });
  };

  const musicXmlRenderer = (xml: any) => {
    const containerRef = useRef(null);

    useEffect(() => {
      const renderMusic = async () => {
        try {
          const parsedData = await parseMusicXml(xml);

          const notes = convertToVexFlowNotes(parsedData);

          const VF = Vex.Flow;
          const div = containerRef.current;
          const renderer = new VF.Renderer(
            div as unknown as HTMLDivElement,
            VF.Renderer.Backends.SVG
          );

          renderer.resize(500, 200);
          const context = renderer.getContext();
          context.setFont("Arial", 10, "").setBackgroundFillStyle("#eed");

          const stave = new VF.Stave(10, 40, 400);
          stave.addClef("treble").setContext(context).draw();

          const voice = new VF.Voice({ num_beats: 4, beat_value: 4 });
          voice.addTickables(notes);

          const formatter = new VF.Formatter()
            .joinVoices([voice])
            .format([voice], 400);
          voice.draw(context, stave);
        } catch (error) {
          console.error("Error rendering MusicXML:", error);
        }
      };
      renderMusic();
    }, [xml]);
    return <div ref={containerRef}></div>;
  };
  return (
    <IonPage>
      <IonContent fullscreen>
        <Container>
          <Center>
            <ButtonGroup>
              <WrapItem>
                <Button
                  onClick={pickXml}
                  colorScheme="cyan"
                  marginTop={5}
                  onChange={handleFileChange}
                >
                  {/* <Input  type="file" ></Input>*/}
                  Load Sheet
                </Button>
              </WrapItem>
              <WrapItem>
                <Button colorScheme="cyan" marginTop={5} onClick={pickAudio}>
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
        <Container>
          <Center>{xmlContent ? musicXmlRenderer(xmlContent) : ""}</Center>
        </Container>
        <Container>
          <VStack>
            <Card>
              
              <CardBody>
                <Center>
                  <BsFileEarmarkMusic size={50} color="red" />
                </Center>
                <Text fontSize={"sm"}>
                  Select a musicXML file to render the sheet music
                </Text>
              </CardBody>
            </Card>

            <Card>
              <CardBody>
                <Center>
                  <FaMusic size={50} color="red" />
                </Center>
                <Text fontSize={"sm"}>Select a recording to analyze</Text>
              </CardBody>
            </Card>
          </VStack>
        </Container>
        <IonHeader collapse="condense">
          <IonToolbar>
            <IonTitle size="large">Home</IonTitle>
          </IonToolbar>
        </IonHeader>
      </IonContent>
    </IonPage>
  );
}
