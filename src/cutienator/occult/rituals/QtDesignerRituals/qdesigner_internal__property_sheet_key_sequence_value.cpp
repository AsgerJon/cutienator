//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#if QT_CONFIG(shortcut)
#include <QtGui/qkeysequence.h>
#endif
#include <QtCore/qstring.h>

//  qdesigner_internal::PropertySheetKeySequenceValue::PropertySheetKeySequen
//      ceValue(const QKeySequence &value, bool translatable, const QString
//      &disambiguation, const QString &comment)
extern "C" Q_DECL_EXPORT
qdesigner_internal::PropertySheetKeySequenceValue *ritual_ZN18qdesigner_internal29PropertySheetKeySequenceValueC1ERK12QKeySequencebRK7QStringS6_(
    const QKeySequence *value,
    bool translatable,
    const QString *disambiguation,
    const QString *comment) {
  return new qdesigner_internal::PropertySheetKeySequenceValue(
      *value,
      translatable,
      *disambiguation,
      *comment);
}

//  qdesigner_internal::PropertySheetKeySequenceValue::PropertySheetKeySequen
//      ceValue(const QKeySequence::StandardKey &standardKey, bool
//      translatable, const QString &disambiguation, const QString &comment)
extern "C" Q_DECL_EXPORT
qdesigner_internal::PropertySheetKeySequenceValue *ritual_ZN18qdesigner_internal29PropertySheetKeySequenceValueC1ERKN12QKeySequence11StandardKeyEbRK7QStringS7_(
    const QKeySequence::StandardKey *standardKey,
    bool translatable,
    const QString *disambiguation,
    const QString *comment) {
  return new qdesigner_internal::PropertySheetKeySequenceValue(
      *standardKey,
      translatable,
      *disambiguation,
      *comment);
}

//  QKeySequence qdesigner_internal::PropertySheetKeySequenceValue::value()
//      const
extern "C" Q_DECL_EXPORT
QKeySequence *ritual_ZNK18qdesigner_internal29PropertySheetKeySequenceValue5valueEv(
    const qdesigner_internal::PropertySheetKeySequenceValue *self) {
  return new QKeySequence(self->value());
}

//  void qdesigner_internal::PropertySheetKeySequenceValue::setValue(const
//      QKeySequence &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal29PropertySheetKeySequenceValue8setValueERK12QKeySequence(
    qdesigner_internal::PropertySheetKeySequenceValue *self,
    const QKeySequence *value) {
  self->setValue(*value);
}

//  QKeySequence::StandardKey
//      qdesigner_internal::PropertySheetKeySequenceValue::standardKey()
//      const
extern "C" Q_DECL_EXPORT
QKeySequence::StandardKey ritual_ZNK18qdesigner_internal29PropertySheetKeySequenceValue11standardKeyEv(
    const qdesigner_internal::PropertySheetKeySequenceValue *self) {
  return self->standardKey();
}

//  void
//      qdesigner_internal::PropertySheetKeySequenceValue::setStandardKey(con
//      st QKeySequence::StandardKey &standardKey)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal29PropertySheetKeySequenceValue14setStandardKeyERKN12QKeySequence11StandardKeyE(
    qdesigner_internal::PropertySheetKeySequenceValue *self,
    const QKeySequence::StandardKey *standardKey) {
  self->setStandardKey(*standardKey);
}

//  bool qdesigner_internal::PropertySheetKeySequenceValue::isStandardKey()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal29PropertySheetKeySequenceValue13isStandardKeyEv(
    const qdesigner_internal::PropertySheetKeySequenceValue *self) {
  return self->isStandardKey();
}

//  bool operator==(const PropertySheetKeySequenceValue &lhs, const
//      PropertySheetKeySequenceValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internaleqERKNS_29PropertySheetKeySequenceValueES2_(
    const qdesigner_internal::PropertySheetKeySequenceValue *lhs,
    const qdesigner_internal::PropertySheetKeySequenceValue *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const PropertySheetKeySequenceValue &lhs, const
//      PropertySheetKeySequenceValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internalneERKNS_29PropertySheetKeySequenceValueES2_(
    const qdesigner_internal::PropertySheetKeySequenceValue *lhs,
    const qdesigner_internal::PropertySheetKeySequenceValue *rhs) {
  return operator!=(*lhs, *rhs);
}

//  qdesigner_internal::PropertySheetKeySequenceValue::~PropertySheetKeySeque
//      nceValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal29PropertySheetKeySequenceValueD1Ev(
    qdesigner_internal::PropertySheetKeySequenceValue *self) {
  delete self;
}
