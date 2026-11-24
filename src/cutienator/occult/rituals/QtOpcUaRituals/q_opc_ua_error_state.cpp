//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuaerrorstate.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuaerrorstate.h>

//  QOpcUaErrorState::QOpcUaErrorState()
extern "C" Q_DECL_EXPORT
QOpcUaErrorState *ritual_ZN16QOpcUaErrorStateC1Ev() {
  return new QOpcUaErrorState();
}

//  QOpcUaErrorState::QOpcUaErrorState(const QOpcUaErrorState &other)
extern "C" Q_DECL_EXPORT
QOpcUaErrorState *ritual_ZN16QOpcUaErrorStateC1ERKS_(
    const QOpcUaErrorState *other) {
  return new QOpcUaErrorState(*other);
}

//  QOpcUaErrorState::~QOpcUaErrorState()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaErrorStateD1Ev(QOpcUaErrorState *self) {
  delete self;
}

//  ConnectionStep QOpcUaErrorState::connectionStep() const
extern "C" Q_DECL_EXPORT
QOpcUaErrorState::ConnectionStep ritual_ZNK16QOpcUaErrorState14connectionStepEv(
    const QOpcUaErrorState *self) {
  return self->connectionStep();
}

//  void QOpcUaErrorState::setConnectionStep(ConnectionStep step)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaErrorState17setConnectionStepENS_14ConnectionStepE(
    QOpcUaErrorState *self,
    QOpcUaErrorState::ConnectionStep step) {
  self->setConnectionStep(step);
}

//  QOpcUa::UaStatusCode QOpcUaErrorState::errorCode() const
extern "C" Q_DECL_EXPORT
QOpcUa::UaStatusCode ritual_ZNK16QOpcUaErrorState9errorCodeEv(
    const QOpcUaErrorState *self) {
  return self->errorCode();
}

//  void QOpcUaErrorState::setErrorCode(QOpcUa::UaStatusCode error)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaErrorState12setErrorCodeEN6QOpcUa12UaStatusCodeE(
    QOpcUaErrorState *self,
    QOpcUa::UaStatusCode error) {
  self->setErrorCode(error);
}

//  bool QOpcUaErrorState::isClientSideError() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QOpcUaErrorState17isClientSideErrorEv(
    const QOpcUaErrorState *self) {
  return self->isClientSideError();
}

//  void QOpcUaErrorState::setClientSideError(bool clientSideError)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaErrorState18setClientSideErrorEb(
    QOpcUaErrorState *self,
    bool clientSideError) {
  self->setClientSideError(clientSideError);
}

//  void QOpcUaErrorState::setIgnoreError(bool ignore)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QOpcUaErrorState14setIgnoreErrorEb(
    QOpcUaErrorState *self,
    bool ignore) {
  self->setIgnoreError(ignore);
}

//  bool QOpcUaErrorState::ignoreError() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QOpcUaErrorState11ignoreErrorEv(
    const QOpcUaErrorState *self) {
  return self->ignoreError();
}
