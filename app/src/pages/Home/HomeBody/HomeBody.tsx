import {
  Container,
  VStack,
  Card,
  CardBody,
  Center,
  Text,
  Image,
  CardFooter,
  Box,
} from "@chakra-ui/react";
import { transform } from "framer-motion";
import { useRef, useEffect, useState } from "react";
import { BsFileEarmarkMusic } from "react-icons/bs";
import { FaMusic } from "react-icons/fa";
import { parseString } from "xml2js";
import { asserts, elements, MusicXML } from "@stringsync/musicxml";
import { OpenSheetMusicDisplay } from "opensheetmusicdisplay";

export default function HomeBody({ xml }: { xml: any }) {
  return (
    <>
      {!xml ? (
        <Container margin={0} position={"absolute"} top={"40%"}>
          <Center>
            <Card h={150}>
              <CardBody marginTop={10}>
                <Text opacity={0.5}>Select a sheet and a recording</Text>
              </CardBody>
            </Card>
          </Center>
        </Container>
      ) : (
        <MusicSheet xml={xml} />
      )}
    </>
  );
}

function MusicSheet({ xml }: { xml: any }) {
  const canvasRef = useRef<HTMLDivElement>(null);
  const [xmlParsed, setXmlParsed] = useState<any>(null);
  useEffect(() => {

    const osmd = new OpenSheetMusicDisplay(canvasRef.current!);
    osmd.setOptions({
      backend: "svg",
      drawTitle: true,
    });
    osmd.load(xml).then(() => {
      osmd.Zoom = 0.5
      osmd.render();
    });
  });

  return (
    <Container>
      <div ref={canvasRef}></div>
    </Container>
  );
}

// const convertToVexFlowNotes = (data: any) => {
//   const notes = data["score-partwise"]["part"][0]["measure"][0]["note"];
//   return notes.map(({ note }: { note: any }) => {
//     const pitch = note["pitch"][0];
//     const step = pitch["step"][0];
//     const octave = pitch["octave"][0];
//     const duration = note["duration"][0];
//     const noteName = `${step}/${octave}`;
//     return new StaveNote({
//       keys: [noteName],
//       duration: duration,
//     });
//   });
// };

// useEffect(() => {
//   const renderMusicXml = async () => {
//     try {
//       const parsedData = await parseXml(xml);
//       const notes = convertToVexFlowNotes(parsedData);
//       const VF = Vex.Flow;
//       const div = divRef.current;
//       const renderer = new VF.Renderer(div!, VF.Renderer.Backends.SVG);

//       renderer.resize(500, 200);
//       const context = renderer.getContext();
//       context.setFont("Arial", 10, "").setBackgroundFillStyle("#eed");

//       const stave = new VF.Stave(10, 40, 400);
//       const voice = new VF.Voice({ num_beats: 4, beat_value: 4 });
//       voice.addTickables(notes);

//       const formatter = new VF.Formatter()
//         .joinVoices([voice])
//         .format([voice], 400);
//       voice.draw(context, stave);
//     } catch (error) {
//       console.error("Error rendering MusicXML:", error);
//     }
//   };
//   renderMusicXml()
// }, [xml]);
