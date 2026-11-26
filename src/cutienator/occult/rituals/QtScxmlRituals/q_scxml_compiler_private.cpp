//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlcompiler_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlcompiler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtScxml/qscxmlerror.h>
#if QT_CONFIG(xmlstream)
#include <QtCore/qxmlstream.h>
#endif
#include <QtCore/qlist.h>

//  QScxmlCompilerPrivate *QScxmlCompilerPrivate::get(QScxmlCompiler
//      *compiler)
extern "C" Q_DECL_EXPORT
QScxmlCompilerPrivate *ritual_ZN21QScxmlCompilerPrivate3getEP14QScxmlCompiler(
    QScxmlCompiler *compiler) {
  return QScxmlCompilerPrivate::get(compiler);
}

//  QScxmlCompilerPrivate::QScxmlCompilerPrivate(QXmlStreamReader *reader)
extern "C" Q_DECL_EXPORT
QScxmlCompilerPrivate *ritual_ZN21QScxmlCompilerPrivateC1EP16QXmlStreamReader(
    QXmlStreamReader *reader) {
  return new QScxmlCompilerPrivate(reader);
}

//  bool QScxmlCompilerPrivate::verifyDocument()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate14verifyDocumentEv(
    QScxmlCompilerPrivate *self) {
  return self->verifyDocument();
}

//  DocumentModel::ScxmlDocument *QScxmlCompilerPrivate::scxmlDocument()
//      const
extern "C" Q_DECL_EXPORT
DocumentModel::ScxmlDocument *ritual_ZNK21QScxmlCompilerPrivate13scxmlDocumentEv(
    const QScxmlCompilerPrivate *self) {
  return self->scxmlDocument();
}

//  QString QScxmlCompilerPrivate::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK21QScxmlCompilerPrivate8fileNameEv(
    const QScxmlCompilerPrivate *self) {
  return new QString(self->fileName());
}

//  void QScxmlCompilerPrivate::setFileName(const QString &fileName)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QScxmlCompilerPrivate11setFileNameERK7QString(
    QScxmlCompilerPrivate *self,
    const QString *fileName) {
  self->setFileName(*fileName);
}

//  QScxmlCompiler::Loader *QScxmlCompilerPrivate::loader() const
extern "C" Q_DECL_EXPORT
QScxmlCompiler::Loader *ritual_ZNK21QScxmlCompilerPrivate6loaderEv(
    const QScxmlCompilerPrivate *self) {
  return self->loader();
}

//  void QScxmlCompilerPrivate::setLoader(QScxmlCompiler::Loader *loader)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QScxmlCompilerPrivate9setLoaderEPN14QScxmlCompiler6LoaderE(
    QScxmlCompilerPrivate *self,
    QScxmlCompiler::Loader *loader) {
  self->setLoader(loader);
}

//  bool QScxmlCompilerPrivate::readDocument()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate12readDocumentEv(
    QScxmlCompilerPrivate *self) {
  return self->readDocument();
}

//  void QScxmlCompilerPrivate::parseSubDocument(DocumentModel::Invoke
//      *parentInvoke, QXmlStreamReader *reader, const QString &fileName)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QScxmlCompilerPrivate16parseSubDocumentEPN13DocumentModel6InvokeEP16QXmlStreamReaderRK7QString(
    QScxmlCompilerPrivate *self,
    DocumentModel::Invoke *parentInvoke,
    QXmlStreamReader *reader,
    const QString *fileName) {
  self->parseSubDocument(parentInvoke, reader, *fileName);
}

//  bool QScxmlCompilerPrivate::parseSubElement(DocumentModel::Invoke
//      *parentInvoke, QXmlStreamReader *reader, const QString &fileName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate15parseSubElementEPN13DocumentModel6InvokeEP16QXmlStreamReaderRK7QString(
    QScxmlCompilerPrivate *self,
    DocumentModel::Invoke *parentInvoke,
    QXmlStreamReader *reader,
    const QString *fileName) {
  return self->parseSubElement(parentInvoke, reader, *fileName);
}

//  QByteArray QScxmlCompilerPrivate::load(const QString &name, bool *ok)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN21QScxmlCompilerPrivate4loadERK7QStringPb(
    QScxmlCompilerPrivate *self,
    const QString *name,
    bool *ok) {
  return new QByteArray(self->load(*name, ok));
}

//  QList<QScxmlError> QScxmlCompilerPrivate::errors() const
extern "C" Q_DECL_EXPORT
QList<QScxmlError> *ritual_ZNK21QScxmlCompilerPrivate6errorsEv(
    const QScxmlCompilerPrivate *self) {
  return new QList<QScxmlError>(self->errors());
}

//  void QScxmlCompilerPrivate::addError(const QString &msg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QScxmlCompilerPrivate8addErrorERK7QString(
    QScxmlCompilerPrivate *self,
    const QString *msg) {
  self->addError(*msg);
}

//  void QScxmlCompilerPrivate::addError(const QString &fileName, const
//      DocumentModel::XmlLocation &location, const QString &msg)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QScxmlCompilerPrivate8addErrorERK7QStringRKN13DocumentModel11XmlLocationES2_(
    QScxmlCompilerPrivate *self,
    const QString *fileName,
    const DocumentModel::XmlLocation *location,
    const QString *msg) {
  self->addError(*fileName, *location, *msg);
}

//  QScxmlStateMachine *QScxmlCompilerPrivate::instantiateStateMachine()
//      const
extern "C" Q_DECL_EXPORT
QScxmlStateMachine *ritual_ZNK21QScxmlCompilerPrivate23instantiateStateMachineEv(
    const QScxmlCompilerPrivate *self) {
  return self->instantiateStateMachine();
}

//  void QScxmlCompilerPrivate::instantiateDataModel(QScxmlStateMachine
//      *stateMachine) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QScxmlCompilerPrivate20instantiateDataModelEP18QScxmlStateMachine(
    const QScxmlCompilerPrivate *self,
    QScxmlStateMachine *stateMachine) {
  self->instantiateDataModel(stateMachine);
}

//  DocumentModel::AbstractState *QScxmlCompilerPrivate::currentParent()
//      const
extern "C" Q_DECL_EXPORT
DocumentModel::AbstractState *ritual_ZNK21QScxmlCompilerPrivate13currentParentEv(
    const QScxmlCompilerPrivate *self) {
  return self->currentParent();
}

//  DocumentModel::XmlLocation QScxmlCompilerPrivate::xmlLocation() const
extern "C" Q_DECL_EXPORT
DocumentModel::XmlLocation *ritual_ZNK21QScxmlCompilerPrivate11xmlLocationEv(
    const QScxmlCompilerPrivate *self) {
  return new DocumentModel::XmlLocation(self->xmlLocation());
}

//  bool QScxmlCompilerPrivate::maybeId(const QXmlStreamAttributes
//      &attributes, QString *id)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate7maybeIdERK20QXmlStreamAttributesP7QString(
    QScxmlCompilerPrivate *self,
    const QXmlStreamAttributes *attributes,
    QString *id) {
  return self->maybeId(*attributes, id);
}

//  DocumentModel::If *QScxmlCompilerPrivate::lastIf()
extern "C" Q_DECL_EXPORT
DocumentModel::If *ritual_ZN21QScxmlCompilerPrivate6lastIfEv(
    QScxmlCompilerPrivate *self) {
  return self->lastIf();
}

//  bool QScxmlCompilerPrivate::checkAttributes(const QXmlStreamAttributes
//      &attributes, const QStringList &requiredNames, const QStringList
//      &optionalNames)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate15checkAttributesERK20QXmlStreamAttributesRK5QListI7QStringES7_(
    QScxmlCompilerPrivate *self,
    const QXmlStreamAttributes *attributes,
    const QList<QString> *requiredNames,
    const QList<QString> *optionalNames) {
  return self->checkAttributes(*attributes, *requiredNames, *optionalNames);
}

//  bool QScxmlCompilerPrivate::preReadElementScxml()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate19preReadElementScxmlEv(
    QScxmlCompilerPrivate *self) {
  return self->preReadElementScxml();
}

//  bool QScxmlCompilerPrivate::preReadElementState()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate19preReadElementStateEv(
    QScxmlCompilerPrivate *self) {
  return self->preReadElementState();
}

//  bool QScxmlCompilerPrivate::preReadElementParallel()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate22preReadElementParallelEv(
    QScxmlCompilerPrivate *self) {
  return self->preReadElementParallel();
}

//  bool QScxmlCompilerPrivate::preReadElementInitial()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate21preReadElementInitialEv(
    QScxmlCompilerPrivate *self) {
  return self->preReadElementInitial();
}

//  bool QScxmlCompilerPrivate::preReadElementTransition()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate24preReadElementTransitionEv(
    QScxmlCompilerPrivate *self) {
  return self->preReadElementTransition();
}

//  bool QScxmlCompilerPrivate::preReadElementFinal()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate19preReadElementFinalEv(
    QScxmlCompilerPrivate *self) {
  return self->preReadElementFinal();
}

//  bool QScxmlCompilerPrivate::preReadElementHistory()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate21preReadElementHistoryEv(
    QScxmlCompilerPrivate *self) {
  return self->preReadElementHistory();
}

//  bool QScxmlCompilerPrivate::preReadElementOnEntry()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate21preReadElementOnEntryEv(
    QScxmlCompilerPrivate *self) {
  return self->preReadElementOnEntry();
}

//  bool QScxmlCompilerPrivate::preReadElementOnExit()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate20preReadElementOnExitEv(
    QScxmlCompilerPrivate *self) {
  return self->preReadElementOnExit();
}

//  bool QScxmlCompilerPrivate::preReadElementRaise()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate19preReadElementRaiseEv(
    QScxmlCompilerPrivate *self) {
  return self->preReadElementRaise();
}

//  bool QScxmlCompilerPrivate::preReadElementIf()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate16preReadElementIfEv(
    QScxmlCompilerPrivate *self) {
  return self->preReadElementIf();
}

//  bool QScxmlCompilerPrivate::preReadElementElseIf()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate20preReadElementElseIfEv(
    QScxmlCompilerPrivate *self) {
  return self->preReadElementElseIf();
}

//  bool QScxmlCompilerPrivate::preReadElementElse()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate18preReadElementElseEv(
    QScxmlCompilerPrivate *self) {
  return self->preReadElementElse();
}

//  bool QScxmlCompilerPrivate::preReadElementForeach()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate21preReadElementForeachEv(
    QScxmlCompilerPrivate *self) {
  return self->preReadElementForeach();
}

//  bool QScxmlCompilerPrivate::preReadElementLog()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate17preReadElementLogEv(
    QScxmlCompilerPrivate *self) {
  return self->preReadElementLog();
}

//  bool QScxmlCompilerPrivate::preReadElementDataModel()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate23preReadElementDataModelEv(
    QScxmlCompilerPrivate *self) {
  return self->preReadElementDataModel();
}

//  bool QScxmlCompilerPrivate::preReadElementData()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate18preReadElementDataEv(
    QScxmlCompilerPrivate *self) {
  return self->preReadElementData();
}

//  bool QScxmlCompilerPrivate::preReadElementAssign()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate20preReadElementAssignEv(
    QScxmlCompilerPrivate *self) {
  return self->preReadElementAssign();
}

//  bool QScxmlCompilerPrivate::preReadElementDoneData()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate22preReadElementDoneDataEv(
    QScxmlCompilerPrivate *self) {
  return self->preReadElementDoneData();
}

//  bool QScxmlCompilerPrivate::preReadElementContent()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate21preReadElementContentEv(
    QScxmlCompilerPrivate *self) {
  return self->preReadElementContent();
}

//  bool QScxmlCompilerPrivate::preReadElementParam()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate19preReadElementParamEv(
    QScxmlCompilerPrivate *self) {
  return self->preReadElementParam();
}

//  bool QScxmlCompilerPrivate::preReadElementScript()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate20preReadElementScriptEv(
    QScxmlCompilerPrivate *self) {
  return self->preReadElementScript();
}

//  bool QScxmlCompilerPrivate::preReadElementSend()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate18preReadElementSendEv(
    QScxmlCompilerPrivate *self) {
  return self->preReadElementSend();
}

//  bool QScxmlCompilerPrivate::preReadElementCancel()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate20preReadElementCancelEv(
    QScxmlCompilerPrivate *self) {
  return self->preReadElementCancel();
}

//  bool QScxmlCompilerPrivate::preReadElementInvoke()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate20preReadElementInvokeEv(
    QScxmlCompilerPrivate *self) {
  return self->preReadElementInvoke();
}

//  bool QScxmlCompilerPrivate::preReadElementFinalize()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate22preReadElementFinalizeEv(
    QScxmlCompilerPrivate *self) {
  return self->preReadElementFinalize();
}

//  bool QScxmlCompilerPrivate::postReadElementScxml()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate20postReadElementScxmlEv(
    QScxmlCompilerPrivate *self) {
  return self->postReadElementScxml();
}

//  bool QScxmlCompilerPrivate::postReadElementState()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate20postReadElementStateEv(
    QScxmlCompilerPrivate *self) {
  return self->postReadElementState();
}

//  bool QScxmlCompilerPrivate::postReadElementParallel()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate23postReadElementParallelEv(
    QScxmlCompilerPrivate *self) {
  return self->postReadElementParallel();
}

//  bool QScxmlCompilerPrivate::postReadElementInitial()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate22postReadElementInitialEv(
    QScxmlCompilerPrivate *self) {
  return self->postReadElementInitial();
}

//  bool QScxmlCompilerPrivate::postReadElementTransition()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate25postReadElementTransitionEv(
    QScxmlCompilerPrivate *self) {
  return self->postReadElementTransition();
}

//  bool QScxmlCompilerPrivate::postReadElementFinal()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate20postReadElementFinalEv(
    QScxmlCompilerPrivate *self) {
  return self->postReadElementFinal();
}

//  bool QScxmlCompilerPrivate::postReadElementHistory()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate22postReadElementHistoryEv(
    QScxmlCompilerPrivate *self) {
  return self->postReadElementHistory();
}

//  bool QScxmlCompilerPrivate::postReadElementOnEntry()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate22postReadElementOnEntryEv(
    QScxmlCompilerPrivate *self) {
  return self->postReadElementOnEntry();
}

//  bool QScxmlCompilerPrivate::postReadElementOnExit()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate21postReadElementOnExitEv(
    QScxmlCompilerPrivate *self) {
  return self->postReadElementOnExit();
}

//  bool QScxmlCompilerPrivate::postReadElementRaise()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate20postReadElementRaiseEv(
    QScxmlCompilerPrivate *self) {
  return self->postReadElementRaise();
}

//  bool QScxmlCompilerPrivate::postReadElementIf()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate17postReadElementIfEv(
    QScxmlCompilerPrivate *self) {
  return self->postReadElementIf();
}

//  bool QScxmlCompilerPrivate::postReadElementElseIf()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate21postReadElementElseIfEv(
    QScxmlCompilerPrivate *self) {
  return self->postReadElementElseIf();
}

//  bool QScxmlCompilerPrivate::postReadElementElse()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate19postReadElementElseEv(
    QScxmlCompilerPrivate *self) {
  return self->postReadElementElse();
}

//  bool QScxmlCompilerPrivate::postReadElementForeach()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate22postReadElementForeachEv(
    QScxmlCompilerPrivate *self) {
  return self->postReadElementForeach();
}

//  bool QScxmlCompilerPrivate::postReadElementLog()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate18postReadElementLogEv(
    QScxmlCompilerPrivate *self) {
  return self->postReadElementLog();
}

//  bool QScxmlCompilerPrivate::postReadElementDataModel()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate24postReadElementDataModelEv(
    QScxmlCompilerPrivate *self) {
  return self->postReadElementDataModel();
}

//  bool QScxmlCompilerPrivate::postReadElementData()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate19postReadElementDataEv(
    QScxmlCompilerPrivate *self) {
  return self->postReadElementData();
}

//  bool QScxmlCompilerPrivate::postReadElementAssign()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate21postReadElementAssignEv(
    QScxmlCompilerPrivate *self) {
  return self->postReadElementAssign();
}

//  bool QScxmlCompilerPrivate::postReadElementDoneData()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate23postReadElementDoneDataEv(
    QScxmlCompilerPrivate *self) {
  return self->postReadElementDoneData();
}

//  bool QScxmlCompilerPrivate::postReadElementContent()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate22postReadElementContentEv(
    QScxmlCompilerPrivate *self) {
  return self->postReadElementContent();
}

//  bool QScxmlCompilerPrivate::postReadElementParam()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate20postReadElementParamEv(
    QScxmlCompilerPrivate *self) {
  return self->postReadElementParam();
}

//  bool QScxmlCompilerPrivate::postReadElementScript()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate21postReadElementScriptEv(
    QScxmlCompilerPrivate *self) {
  return self->postReadElementScript();
}

//  bool QScxmlCompilerPrivate::postReadElementSend()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate19postReadElementSendEv(
    QScxmlCompilerPrivate *self) {
  return self->postReadElementSend();
}

//  bool QScxmlCompilerPrivate::postReadElementCancel()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate21postReadElementCancelEv(
    QScxmlCompilerPrivate *self) {
  return self->postReadElementCancel();
}

//  bool QScxmlCompilerPrivate::postReadElementInvoke()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate21postReadElementInvokeEv(
    QScxmlCompilerPrivate *self) {
  return self->postReadElementInvoke();
}

//  bool QScxmlCompilerPrivate::postReadElementFinalize()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate23postReadElementFinalizeEv(
    QScxmlCompilerPrivate *self) {
  return self->postReadElementFinalize();
}

//  bool QScxmlCompilerPrivate::readElement()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate11readElementEv(
    QScxmlCompilerPrivate *self) {
  return self->readElement();
}

//  void QScxmlCompilerPrivate::resetDocument()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QScxmlCompilerPrivate13resetDocumentEv(
    QScxmlCompilerPrivate *self) {
  self->resetDocument();
}

//  void QScxmlCompilerPrivate::currentStateUp()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QScxmlCompilerPrivate14currentStateUpEv(
    QScxmlCompilerPrivate *self) {
  self->currentStateUp();
}

//  bool QScxmlCompilerPrivate::flushInstruction()
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate16flushInstructionEv(
    QScxmlCompilerPrivate *self) {
  return self->flushInstruction();
}

//  bool QScxmlCompilerPrivate::checkAttributes(const QXmlStreamAttributes
//      &attributes, QScxmlCompilerPrivate::ParserState::Kind kind)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QScxmlCompilerPrivate15checkAttributesERK20QXmlStreamAttributesNS_11ParserState4KindE(
    QScxmlCompilerPrivate *self,
    const QXmlStreamAttributes *attributes,
    QScxmlCompilerPrivate::ParserState::Kind kind) {
  return self->checkAttributes(*attributes, kind);
}

//  ParserState &QScxmlCompilerPrivate::current()
extern "C" Q_DECL_EXPORT
QScxmlCompilerPrivate::ParserState *ritual_ZN21QScxmlCompilerPrivate7currentEv(
    QScxmlCompilerPrivate *self) {
  return &(self->current());
}

//  ParserState &QScxmlCompilerPrivate::previous()
extern "C" Q_DECL_EXPORT
QScxmlCompilerPrivate::ParserState *ritual_ZN21QScxmlCompilerPrivate8previousEv(
    QScxmlCompilerPrivate *self) {
  return &(self->previous());
}

//  bool QScxmlCompilerPrivate::hasPrevious() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QScxmlCompilerPrivate11hasPreviousEv(
    const QScxmlCompilerPrivate *self) {
  return self->hasPrevious();
}
