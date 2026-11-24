//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/qscxmlcompiler.h, Qt 6.12.0. Changes made here are lost.
#include <QtScxml/qscxmlcompiler.h>
#include <QtCore/qstring.h>
#include <QtScxml/qscxmlerror.h>
#include <QtCore/qlist.h>

//  QScxmlCompiler::QScxmlCompiler(QXmlStreamReader *xmlReader)
extern "C" Q_DECL_EXPORT
QScxmlCompiler *ritual_ZN14QScxmlCompilerC1EP16QXmlStreamReader(
    QXmlStreamReader *xmlReader) {
  return new QScxmlCompiler(xmlReader);
}

//  QScxmlCompiler::~QScxmlCompiler()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScxmlCompilerD1Ev(QScxmlCompiler *self) {
  delete self;
}

//  QString QScxmlCompiler::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QScxmlCompiler8fileNameEv(const QScxmlCompiler *self) {
  return new QString(self->fileName());
}

//  void QScxmlCompiler::setFileName(const QString &fileName)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScxmlCompiler11setFileNameERK7QString(
    QScxmlCompiler *self,
    const QString *fileName) {
  self->setFileName(*fileName);
}

//  Loader *QScxmlCompiler::loader() const
extern "C" Q_DECL_EXPORT
QScxmlCompiler::Loader *ritual_ZNK14QScxmlCompiler6loaderEv(
    const QScxmlCompiler *self) {
  return self->loader();
}

//  void QScxmlCompiler::setLoader(Loader *newLoader)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScxmlCompiler9setLoaderEPNS_6LoaderE(
    QScxmlCompiler *self,
    QScxmlCompiler::Loader *newLoader) {
  self->setLoader(newLoader);
}

//  QScxmlStateMachine *QScxmlCompiler::compile()
extern "C" Q_DECL_EXPORT
QScxmlStateMachine *ritual_ZN14QScxmlCompiler7compileEv(
    QScxmlCompiler *self) {
  return self->compile();
}

//  QList<QScxmlError> QScxmlCompiler::errors() const
extern "C" Q_DECL_EXPORT
QList<QScxmlError> *ritual_ZNK14QScxmlCompiler6errorsEv(
    const QScxmlCompiler *self) {
  return new QList<QScxmlError>(self->errors());
}
