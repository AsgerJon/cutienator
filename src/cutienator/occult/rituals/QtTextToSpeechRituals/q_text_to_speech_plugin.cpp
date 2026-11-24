//  Written by dev_tooling.RitualGenerator from the records of
//  QtTextToSpeech/qtexttospeechplugin.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtTextToSpeech/qtexttospeechplugin.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  QTextToSpeechPlugin::~QTextToSpeechPlugin()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextToSpeechPluginD1Ev(QTextToSpeechPlugin *self) {
  delete self;
}

//  QTextToSpeechEngine *QTextToSpeechPlugin::createTextToSpeechEngine(const
//      QVariantMap &parameters, QObject *parent, QString *errorString) const
extern "C" Q_DECL_EXPORT
QTextToSpeechEngine *ritual_ZNK19QTextToSpeechPlugin24createTextToSpeechEngineERK4QMapI7QString8QVariantEP7QObjectPS1_(
    const QTextToSpeechPlugin *self,
    const QMap<QString, QVariant> *parameters,
    QObject *parent,
    QString *errorString) {
  return self->createTextToSpeechEngine(*parameters, parent, errorString);
}
