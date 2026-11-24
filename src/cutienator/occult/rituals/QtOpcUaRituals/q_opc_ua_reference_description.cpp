//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuareferencedescription.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpcUa/qopcuareferencedescription.h>
#include <QtCore/qstring.h>
#include <QtOpcUa/qopcuaexpandednodeid.h>
#include <QtOpcUa/qopcuaqualifiedname.h>
#include <QtOpcUa/qopcualocalizedtext.h>
#include <QtCore/qlist.h>

//  QOpcUaReferenceDescription::QOpcUaReferenceDescription()
extern "C" Q_DECL_EXPORT
QOpcUaReferenceDescription *ritual_ZN26QOpcUaReferenceDescriptionC1Ev() {
  return new QOpcUaReferenceDescription();
}

//  QOpcUaReferenceDescription::QOpcUaReferenceDescription(const
//      QOpcUaReferenceDescription &other)
extern "C" Q_DECL_EXPORT
QOpcUaReferenceDescription *ritual_ZN26QOpcUaReferenceDescriptionC1ERKS_(
    const QOpcUaReferenceDescription *other) {
  return new QOpcUaReferenceDescription(*other);
}

//  QOpcUaReferenceDescription::~QOpcUaReferenceDescription()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaReferenceDescriptionD1Ev(
    QOpcUaReferenceDescription *self) {
  delete self;
}

//  QString QOpcUaReferenceDescription::refTypeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK26QOpcUaReferenceDescription9refTypeIdEv(
    const QOpcUaReferenceDescription *self) {
  return new QString(self->refTypeId());
}

//  void QOpcUaReferenceDescription::setRefTypeId(const QString &refTypeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaReferenceDescription12setRefTypeIdERK7QString(
    QOpcUaReferenceDescription *self,
    const QString *refTypeId) {
  self->setRefTypeId(*refTypeId);
}

//  QOpcUaExpandedNodeId QOpcUaReferenceDescription::targetNodeId() const
extern "C" Q_DECL_EXPORT
QOpcUaExpandedNodeId *ritual_ZNK26QOpcUaReferenceDescription12targetNodeIdEv(
    const QOpcUaReferenceDescription *self) {
  return new QOpcUaExpandedNodeId(self->targetNodeId());
}

//  void QOpcUaReferenceDescription::setTargetNodeId(const
//      QOpcUaExpandedNodeId &targetNodeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaReferenceDescription15setTargetNodeIdERK20QOpcUaExpandedNodeId(
    QOpcUaReferenceDescription *self,
    const QOpcUaExpandedNodeId *targetNodeId) {
  self->setTargetNodeId(*targetNodeId);
}

//  QOpcUaQualifiedName QOpcUaReferenceDescription::browseName() const
extern "C" Q_DECL_EXPORT
QOpcUaQualifiedName *ritual_ZNK26QOpcUaReferenceDescription10browseNameEv(
    const QOpcUaReferenceDescription *self) {
  return new QOpcUaQualifiedName(self->browseName());
}

//  void QOpcUaReferenceDescription::setBrowseName(const QOpcUaQualifiedName
//      &browseName)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaReferenceDescription13setBrowseNameERK19QOpcUaQualifiedName(
    QOpcUaReferenceDescription *self,
    const QOpcUaQualifiedName *browseName) {
  self->setBrowseName(*browseName);
}

//  QOpcUaLocalizedText QOpcUaReferenceDescription::displayName() const
extern "C" Q_DECL_EXPORT
QOpcUaLocalizedText *ritual_ZNK26QOpcUaReferenceDescription11displayNameEv(
    const QOpcUaReferenceDescription *self) {
  return new QOpcUaLocalizedText(self->displayName());
}

//  void QOpcUaReferenceDescription::setDisplayName(const QOpcUaLocalizedText
//      &displayName)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaReferenceDescription14setDisplayNameERK19QOpcUaLocalizedText(
    QOpcUaReferenceDescription *self,
    const QOpcUaLocalizedText *displayName) {
  self->setDisplayName(*displayName);
}

//  QOpcUa::NodeClass QOpcUaReferenceDescription::nodeClass() const
extern "C" Q_DECL_EXPORT
QOpcUa::NodeClass ritual_ZNK26QOpcUaReferenceDescription9nodeClassEv(
    const QOpcUaReferenceDescription *self) {
  return self->nodeClass();
}

//  void QOpcUaReferenceDescription::setNodeClass(QOpcUa::NodeClass
//      nodeClass)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaReferenceDescription12setNodeClassEN6QOpcUa9NodeClassE(
    QOpcUaReferenceDescription *self,
    QOpcUa::NodeClass nodeClass) {
  self->setNodeClass(nodeClass);
}

//  void QOpcUaReferenceDescription::setIsForwardReference(bool
//      isForwardReference)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaReferenceDescription21setIsForwardReferenceEb(
    QOpcUaReferenceDescription *self,
    bool isForwardReference) {
  self->setIsForwardReference(isForwardReference);
}

//  bool QOpcUaReferenceDescription::isForwardReference() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QOpcUaReferenceDescription18isForwardReferenceEv(
    const QOpcUaReferenceDescription *self) {
  return self->isForwardReference();
}

//  void QOpcUaReferenceDescription::setTypeDefinition(const
//      QOpcUaExpandedNodeId &typeDefinition)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QOpcUaReferenceDescription17setTypeDefinitionERK20QOpcUaExpandedNodeId(
    QOpcUaReferenceDescription *self,
    const QOpcUaExpandedNodeId *typeDefinition) {
  self->setTypeDefinition(*typeDefinition);
}

//  QOpcUaExpandedNodeId QOpcUaReferenceDescription::typeDefinition() const
extern "C" Q_DECL_EXPORT
QOpcUaExpandedNodeId *ritual_ZNK26QOpcUaReferenceDescription14typeDefinitionEv(
    const QOpcUaReferenceDescription *self) {
  return new QOpcUaExpandedNodeId(self->typeDefinition());
}

//  QList<QOpcUaReferenceDescription>::QList()
extern "C" Q_DECL_EXPORT
QList<QOpcUaReferenceDescription> *ritual_list_make_QOpcUaReferenceDescription() {
  return new QList<QOpcUaReferenceDescription>();
}

//  void QList<QOpcUaReferenceDescription>::append(const
//      QOpcUaReferenceDescription &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QOpcUaReferenceDescription(
    QList<QOpcUaReferenceDescription> *self,
    const QOpcUaReferenceDescription *element) {
  self->append(*element);
}

//  qsizetype QList<QOpcUaReferenceDescription>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QOpcUaReferenceDescription(
    const QList<QOpcUaReferenceDescription> *self) {
  return self->size();
}

//  const QOpcUaReferenceDescription
//      &QList<QOpcUaReferenceDescription>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QOpcUaReferenceDescription *ritual_list_at_QOpcUaReferenceDescription(
    const QList<QOpcUaReferenceDescription> *self,
    long long index) {
  return new QOpcUaReferenceDescription(self->at(index));
}

//  QList<QOpcUaReferenceDescription>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QOpcUaReferenceDescription(
    QList<QOpcUaReferenceDescription> *self) {
  delete self;
}
