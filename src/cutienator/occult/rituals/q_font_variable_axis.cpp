//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qfontvariableaxis.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qfontvariableaxis.h>
#include <QtGui/qfont.h>
#include <QtCore/qstring.h>

//  QFontVariableAxis::QFontVariableAxis()
extern "C" Q_DECL_EXPORT
QFontVariableAxis *ritual_ZN17QFontVariableAxisC1Ev() {
  return new QFontVariableAxis();
}

//  QFontVariableAxis::QFontVariableAxis(const QFontVariableAxis &axis)
extern "C" Q_DECL_EXPORT
QFontVariableAxis *ritual_ZN17QFontVariableAxisC1ERKS_(
    const QFontVariableAxis *axis) {
  return new QFontVariableAxis(*axis);
}

//  QFontVariableAxis::~QFontVariableAxis()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFontVariableAxisD1Ev(QFontVariableAxis *self) {
  delete self;
}

//  QFont::Tag QFontVariableAxis::tag() const
extern "C" Q_DECL_EXPORT
QFont::Tag *ritual_ZNK17QFontVariableAxis3tagEv(
    const QFontVariableAxis *self) {
  return new QFont::Tag(self->tag());
}

//  void QFontVariableAxis::setTag(QFont::Tag tag)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFontVariableAxis6setTagEN5QFont3TagE(
    QFontVariableAxis *self,
    const QFont::Tag *tag) {
  self->setTag(*tag);
}

//  QString QFontVariableAxis::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QFontVariableAxis4nameEv(
    const QFontVariableAxis *self) {
  return new QString(self->name());
}

//  void QFontVariableAxis::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFontVariableAxis7setNameERK7QString(
    QFontVariableAxis *self,
    const QString *name) {
  self->setName(*name);
}

//  qreal QFontVariableAxis::minimumValue() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QFontVariableAxis12minimumValueEv(
    const QFontVariableAxis *self) {
  return self->minimumValue();
}

//  void QFontVariableAxis::setMinimumValue(qreal minimumValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFontVariableAxis15setMinimumValueEd(
    QFontVariableAxis *self,
    qreal minimumValue) {
  self->setMinimumValue(minimumValue);
}

//  qreal QFontVariableAxis::maximumValue() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QFontVariableAxis12maximumValueEv(
    const QFontVariableAxis *self) {
  return self->maximumValue();
}

//  void QFontVariableAxis::setMaximumValue(qreal maximumValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFontVariableAxis15setMaximumValueEd(
    QFontVariableAxis *self,
    qreal maximumValue) {
  self->setMaximumValue(maximumValue);
}

//  qreal QFontVariableAxis::defaultValue() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QFontVariableAxis12defaultValueEv(
    const QFontVariableAxis *self) {
  return self->defaultValue();
}

//  void QFontVariableAxis::setDefaultValue(qreal defaultValue)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QFontVariableAxis15setDefaultValueEd(
    QFontVariableAxis *self,
    qreal defaultValue) {
  self->setDefaultValue(defaultValue);
}
