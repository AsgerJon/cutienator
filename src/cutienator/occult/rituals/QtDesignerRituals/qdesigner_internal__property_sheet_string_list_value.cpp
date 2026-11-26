//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  qdesigner_internal::PropertySheetStringListValue::PropertySheetStringList
//      Value(const QStringList &value, bool translatable, const QString
//      &disambiguation, const QString &comment)
extern "C" Q_DECL_EXPORT
qdesigner_internal::PropertySheetStringListValue *ritual_ZN18qdesigner_internal28PropertySheetStringListValueC1ERK5QListI7QStringEbRKS2_S7_(
    const QList<QString> *value,
    bool translatable,
    const QString *disambiguation,
    const QString *comment) {
  return new qdesigner_internal::PropertySheetStringListValue(
      *value,
      translatable,
      *disambiguation,
      *comment);
}

//  QStringList qdesigner_internal::PropertySheetStringListValue::value()
//      const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18qdesigner_internal28PropertySheetStringListValue5valueEv(
    const qdesigner_internal::PropertySheetStringListValue *self) {
  return new QList<QString>(self->value());
}

//  void qdesigner_internal::PropertySheetStringListValue::setValue(const
//      QStringList &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal28PropertySheetStringListValue8setValueERK5QListI7QStringE(
    qdesigner_internal::PropertySheetStringListValue *self,
    const QList<QString> *value) {
  self->setValue(*value);
}

//  bool operator==(const PropertySheetStringListValue &lhs, const
//      PropertySheetStringListValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internaleqERKNS_28PropertySheetStringListValueES2_(
    const qdesigner_internal::PropertySheetStringListValue *lhs,
    const qdesigner_internal::PropertySheetStringListValue *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const PropertySheetStringListValue &lhs, const
//      PropertySheetStringListValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internalneERKNS_28PropertySheetStringListValueES2_(
    const qdesigner_internal::PropertySheetStringListValue *lhs,
    const qdesigner_internal::PropertySheetStringListValue *rhs) {
  return operator!=(*lhs, *rhs);
}

//  qdesigner_internal::PropertySheetStringListValue::~PropertySheetStringLis
//      tValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal28PropertySheetStringListValueD1Ev(
    qdesigner_internal::PropertySheetStringListValue *self) {
  delete self;
}
