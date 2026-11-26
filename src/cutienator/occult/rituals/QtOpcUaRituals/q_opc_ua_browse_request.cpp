//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuabrowserequest.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuabrowserequest.h>
#include <QtCore/qstring.h>

//  QOpcUaBrowseRequest::QOpcUaBrowseRequest()
extern "C" Q_DECL_EXPORT
QOpcUaBrowseRequest *ritual_ZN19QOpcUaBrowseRequestC1Ev() {
  return new QOpcUaBrowseRequest();
}

//  QOpcUaBrowseRequest::QOpcUaBrowseRequest(const QOpcUaBrowseRequest
//      &other)
extern "C" Q_DECL_EXPORT
QOpcUaBrowseRequest *ritual_ZN19QOpcUaBrowseRequestC1ERKS_(
    const QOpcUaBrowseRequest *other) {
  return new QOpcUaBrowseRequest(*other);
}

//  QOpcUaBrowseRequest &QOpcUaBrowseRequest::operator=(const
//      QOpcUaBrowseRequest &rhs)
extern "C" Q_DECL_EXPORT
QOpcUaBrowseRequest *ritual_ZN19QOpcUaBrowseRequestaSERKS_(
    QOpcUaBrowseRequest *self,
    const QOpcUaBrowseRequest *rhs) {
  return &(self->operator=(*rhs));
}

//  QOpcUaBrowseRequest::~QOpcUaBrowseRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpcUaBrowseRequestD1Ev(QOpcUaBrowseRequest *self) {
  delete self;
}

//  QOpcUaBrowseRequest::BrowseDirection
//      QOpcUaBrowseRequest::browseDirection() const
extern "C" Q_DECL_EXPORT
QOpcUaBrowseRequest::BrowseDirection ritual_ZNK19QOpcUaBrowseRequest15browseDirectionEv(
    const QOpcUaBrowseRequest *self) {
  return self->browseDirection();
}

//  void QOpcUaBrowseRequest::setBrowseDirection(const
//      QOpcUaBrowseRequest::BrowseDirection &browseDirection)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpcUaBrowseRequest18setBrowseDirectionERKNS_15BrowseDirectionE(
    QOpcUaBrowseRequest *self,
    const QOpcUaBrowseRequest::BrowseDirection *browseDirection) {
  self->setBrowseDirection(*browseDirection);
}

//  QString QOpcUaBrowseRequest::referenceTypeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QOpcUaBrowseRequest15referenceTypeIdEv(
    const QOpcUaBrowseRequest *self) {
  return new QString(self->referenceTypeId());
}

//  void QOpcUaBrowseRequest::setReferenceTypeId(const QString
//      &referenceTypeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpcUaBrowseRequest18setReferenceTypeIdERK7QString(
    QOpcUaBrowseRequest *self,
    const QString *referenceTypeId) {
  self->setReferenceTypeId(*referenceTypeId);
}

//  void QOpcUaBrowseRequest::setReferenceTypeId(QOpcUa::ReferenceTypeId
//      referenceTypeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpcUaBrowseRequest18setReferenceTypeIdEN6QOpcUa15ReferenceTypeIdE(
    QOpcUaBrowseRequest *self,
    QOpcUa::ReferenceTypeId referenceTypeId) {
  self->setReferenceTypeId(referenceTypeId);
}

//  bool QOpcUaBrowseRequest::includeSubtypes() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QOpcUaBrowseRequest15includeSubtypesEv(
    const QOpcUaBrowseRequest *self) {
  return self->includeSubtypes();
}

//  void QOpcUaBrowseRequest::setIncludeSubtypes(bool includeSubtypes)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpcUaBrowseRequest18setIncludeSubtypesEb(
    QOpcUaBrowseRequest *self,
    bool includeSubtypes) {
  self->setIncludeSubtypes(includeSubtypes);
}

//  QOpcUa::NodeClasses QOpcUaBrowseRequest::nodeClassMask() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QOpcUaBrowseRequest13nodeClassMaskEv(
    const QOpcUaBrowseRequest *self) {
  return static_cast<int>(self->nodeClassMask().toInt());
}

//  void QOpcUaBrowseRequest::setNodeClassMask(const QOpcUa::NodeClasses
//      &nodeClassMask)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpcUaBrowseRequest16setNodeClassMaskERK6QFlagsIN6QOpcUa9NodeClassEE(
    QOpcUaBrowseRequest *self,
    const QOpcUa::NodeClasses *nodeClassMask) {
  self->setNodeClassMask(*nodeClassMask);
}
