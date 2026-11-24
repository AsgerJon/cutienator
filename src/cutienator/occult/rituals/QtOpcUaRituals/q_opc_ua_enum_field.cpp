//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuaenumfield.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuaenumfield.h>
#include <QtCore/qvariant.h>
#include <QtOpcUa/qopcualocalizedtext.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  QOpcUaEnumField::QOpcUaEnumField()
extern "C" Q_DECL_EXPORT
QOpcUaEnumField *ritual_ZN15QOpcUaEnumFieldC1Ev() {
  return new QOpcUaEnumField();
}

//  QOpcUaEnumField::QOpcUaEnumField(const QOpcUaEnumField &other)
extern "C" Q_DECL_EXPORT
QOpcUaEnumField *ritual_ZN15QOpcUaEnumFieldC1ERKS_(
    const QOpcUaEnumField *other) {
  return new QOpcUaEnumField(*other);
}

//  QVariant QOpcUaEnumField::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK15QOpcUaEnumFieldcv8QVariantEv(
    const QOpcUaEnumField *self) {
  return new QVariant(self->operator QVariant());
}

//  QOpcUaEnumField::~QOpcUaEnumField()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaEnumFieldD1Ev(QOpcUaEnumField *self) {
  delete self;
}

//  qint64 QOpcUaEnumField::value() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK15QOpcUaEnumField5valueEv(const QOpcUaEnumField *self) {
  return self->value();
}

//  void QOpcUaEnumField::setValue(qint64 value)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaEnumField8setValueEx(
    QOpcUaEnumField *self,
    qint64 value) {
  self->setValue(value);
}

//  QOpcUaLocalizedText QOpcUaEnumField::displayName() const
extern "C" Q_DECL_EXPORT
QOpcUaLocalizedText *ritual_ZNK15QOpcUaEnumField11displayNameEv(
    const QOpcUaEnumField *self) {
  return new QOpcUaLocalizedText(self->displayName());
}

//  void QOpcUaEnumField::setDisplayName(const QOpcUaLocalizedText
//      &displayName)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaEnumField14setDisplayNameERK19QOpcUaLocalizedText(
    QOpcUaEnumField *self,
    const QOpcUaLocalizedText *displayName) {
  self->setDisplayName(*displayName);
}

//  QOpcUaLocalizedText QOpcUaEnumField::description() const
extern "C" Q_DECL_EXPORT
QOpcUaLocalizedText *ritual_ZNK15QOpcUaEnumField11descriptionEv(
    const QOpcUaEnumField *self) {
  return new QOpcUaLocalizedText(self->description());
}

//  void QOpcUaEnumField::setDescription(const QOpcUaLocalizedText
//      &description)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaEnumField14setDescriptionERK19QOpcUaLocalizedText(
    QOpcUaEnumField *self,
    const QOpcUaLocalizedText *description) {
  self->setDescription(*description);
}

//  QString QOpcUaEnumField::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QOpcUaEnumField4nameEv(const QOpcUaEnumField *self) {
  return new QString(self->name());
}

//  void QOpcUaEnumField::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QOpcUaEnumField7setNameERK7QString(
    QOpcUaEnumField *self,
    const QString *name) {
  self->setName(*name);
}

//  bool operator==(const QOpcUaEnumField &lhs, const QOpcUaEnumField &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK15QOpcUaEnumFieldS1_(
    const QOpcUaEnumField *lhs,
    const QOpcUaEnumField *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QOpcUaEnumField &lhs, const QOpcUaEnumField &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK15QOpcUaEnumFieldS1_(
    const QOpcUaEnumField *lhs,
    const QOpcUaEnumField *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QList<QOpcUaEnumField>::QList()
extern "C" Q_DECL_EXPORT
QList<QOpcUaEnumField> *ritual_list_make_QOpcUaEnumField() {
  return new QList<QOpcUaEnumField>();
}

//  void QList<QOpcUaEnumField>::append(const QOpcUaEnumField &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QOpcUaEnumField(
    QList<QOpcUaEnumField> *self,
    const QOpcUaEnumField *element) {
  self->append(*element);
}

//  qsizetype QList<QOpcUaEnumField>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QOpcUaEnumField(
    const QList<QOpcUaEnumField> *self) {
  return self->size();
}

//  const QOpcUaEnumField &QList<QOpcUaEnumField>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QOpcUaEnumField *ritual_list_at_QOpcUaEnumField(
    const QList<QOpcUaEnumField> *self,
    long long index) {
  return new QOpcUaEnumField(self->at(index));
}

//  QList<QOpcUaEnumField>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QOpcUaEnumField(QList<QOpcUaEnumField> *self) {
  delete self;
}
