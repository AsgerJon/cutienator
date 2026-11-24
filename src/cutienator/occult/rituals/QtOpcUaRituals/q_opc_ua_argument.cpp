//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuaargument.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuaargument.h>
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtOpcUa/qopcualocalizedtext.h>

//  QOpcUaArgument::QOpcUaArgument()
extern "C" Q_DECL_EXPORT
QOpcUaArgument *ritual_ZN14QOpcUaArgumentC1Ev() {
  return new QOpcUaArgument();
}

//  QOpcUaArgument::QOpcUaArgument(const QOpcUaArgument &rhs)
extern "C" Q_DECL_EXPORT
QOpcUaArgument *ritual_ZN14QOpcUaArgumentC1ERKS_(const QOpcUaArgument *rhs) {
  return new QOpcUaArgument(*rhs);
}

//  bool QOpcUaArgument::operator==(const QOpcUaArgument &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QOpcUaArgumenteqERKS_(
    const QOpcUaArgument *self,
    const QOpcUaArgument *other) {
  return self->operator==(*other);
}

//  QVariant QOpcUaArgument::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK14QOpcUaArgumentcv8QVariantEv(
    const QOpcUaArgument *self) {
  return new QVariant(self->operator QVariant());
}

//  QOpcUaArgument::~QOpcUaArgument()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpcUaArgumentD1Ev(QOpcUaArgument *self) {
  delete self;
}

//  QString QOpcUaArgument::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QOpcUaArgument4nameEv(const QOpcUaArgument *self) {
  return new QString(self->name());
}

//  void QOpcUaArgument::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpcUaArgument7setNameERK7QString(
    QOpcUaArgument *self,
    const QString *name) {
  self->setName(*name);
}

//  QString QOpcUaArgument::dataTypeId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QOpcUaArgument10dataTypeIdEv(
    const QOpcUaArgument *self) {
  return new QString(self->dataTypeId());
}

//  void QOpcUaArgument::setDataTypeId(const QString &dataTypeId)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpcUaArgument13setDataTypeIdERK7QString(
    QOpcUaArgument *self,
    const QString *dataTypeId) {
  self->setDataTypeId(*dataTypeId);
}

//  qint32 QOpcUaArgument::valueRank() const
extern "C" Q_DECL_EXPORT
qint32 ritual_ZNK14QOpcUaArgument9valueRankEv(const QOpcUaArgument *self) {
  return self->valueRank();
}

//  void QOpcUaArgument::setValueRank(qint32 valueRank)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpcUaArgument12setValueRankEi(
    QOpcUaArgument *self,
    qint32 valueRank) {
  self->setValueRank(valueRank);
}

//  QOpcUaLocalizedText QOpcUaArgument::description() const
extern "C" Q_DECL_EXPORT
QOpcUaLocalizedText *ritual_ZNK14QOpcUaArgument11descriptionEv(
    const QOpcUaArgument *self) {
  return new QOpcUaLocalizedText(self->description());
}

//  void QOpcUaArgument::setDescription(const QOpcUaLocalizedText
//      &description)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpcUaArgument14setDescriptionERK19QOpcUaLocalizedText(
    QOpcUaArgument *self,
    const QOpcUaLocalizedText *description) {
  self->setDescription(*description);
}
