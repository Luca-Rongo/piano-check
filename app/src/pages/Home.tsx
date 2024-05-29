import {
  IonContent,
  IonHeader,
  IonPage,
  IonTitle,
  IonToolbar,
} from "@ionic/react";
import ExploreContainer from "../components/ExploreContainer";
import { Button, ButtonGroup, Center, Icon, WrapItem } from "@chakra-ui/react";
import { Container } from "@chakra-ui/react";
import "./Home.css";
import { Search2Icon } from "@chakra-ui/icons";
import { Vex } from "vexflow";
import { createElement } from "react";
import { Filesystem, Directory } from '@capacitor/filesystem';
import { FilePicker } from "@capawesome/capacitor-file-picker";

const Home: React.FC = () => {
  const pickXml = async () => {
    const result = await FilePicker.pickFiles({
      types: ['.mxl']
    });
  };
  const pickAudio = async () => {
    const result = await FilePicker.pickFiles({
      types: ['audio/*']

    });
  };
  // const div = createElement(
  //   "div",
  //   (onload = function () {
  //     const { Renderer, Stave } = Vex.Flow;
  //     // const renderer = new Renderer(, Renderer.Backends.SVG);

  //     // renderer.resize(500, 500);
  //     // const context = renderer.getContext();
  //     // context.setFont("Arial", 10);

  //     // const stave = new Stave(10, 40, 400);

  //     // stave.addClef("treble").addTimeSignature("4/4");

  //     // stave.setContext(context).draw();
  //   })
  // );
  return (
    <IonPage>
      <IonContent fullscreen>
        <Container>
          <Center>
            <ButtonGroup>
              <WrapItem>
                <Button colorScheme="cyan" marginTop={5} onClick={pickXml}>
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
          <Center>
            {/* <div
              onLoad={ () => {
                const { Renderer, Stave } = Vex.Flow;
                const renderer = new Renderer(this, Renderer.Backends.SVG);

                renderer.resize(500, 500);
                const context = renderer.getContext();
                context.setFont("Arial", 10);

                const stave = new Stave(10, 40, 400);

                stave.addClef("treble").addTimeSignature("4/4");

                stave.setContext(context).draw();
              }}
            ></div> */}
          </Center>
        </Container>
        <IonHeader collapse="condense">
          <IonToolbar>
            <IonTitle size="large">Home</IonTitle>
          </IonToolbar>
        </IonHeader>
      </IonContent>
    </IonPage>
  );
};

export default Home;
