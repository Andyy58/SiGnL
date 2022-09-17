import pyttsx3 as tts
import sounddevice as sd
import soundfile as sf


class Output:
    def __init__(self):
        self.engine = tts.init()
        self.voices = self.engine.getProperty('voices')
        self.output_device = sd.default.device[1]

    @staticmethod
    def get_output_devices():
        host_api = sd.query_hostapis()[0]
        devices = []
        for d in sd.query_devices():
            if d['index'] in host_api['devices'] and d['max_input_channels'] == 0 and d['max_output_channels'] > 0:
                name = d['name']
                if name.find('(') != -1:
                    name = name[:name.find('(')]
                elif name.find('-') != -1:
                    name = name[:name.find('-')]
                devices.append({'name': name.strip(), 'index': d['index']})
        return devices

    def set_output_device(self, index):
        self.output_device = index

    def set_gender(self, gender):
        if gender == 'M':
            self.engine.setProperty('voice', self.voices[0].id)
        else:
            self.engine.setProperty('voice', self.voices[1].id)

    def speak(self, out):
        self.engine.save_to_file(out, 'static/output/output.mp3')
        self.engine.runAndWait()
        data, fs = sf.read('static/output/output.mp3', dtype='float32')
        sd.play(data, fs, device=self.output_device)
        status = sd.wait()
