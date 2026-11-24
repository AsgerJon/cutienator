//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/qqmlsa.h, Qt 6.12.0. Changes made here are lost.
#include <QtQmlCompiler/qqmlsa.h>
#include <QtCore/qstring.h>

//  FixSuggestionPrivate *QQmlSA::FixSuggestion::d_func()
extern "C" Q_DECL_EXPORT
QQmlSA::FixSuggestionPrivate *ritual_ZN6QQmlSA13FixSuggestion6d_funcEv(
    QQmlSA::FixSuggestion *self) {
  return self->d_func();
}

//  const FixSuggestionPrivate *QQmlSA::FixSuggestion::d_func() const
extern "C" Q_DECL_EXPORT
const QQmlSA::FixSuggestionPrivate *ritual_ZNK6QQmlSA13FixSuggestion6d_funcEv(
    const QQmlSA::FixSuggestion *self) {
  return self->d_func();
}

//  QString QQmlSA::FixSuggestion::description() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK6QQmlSA13FixSuggestion11descriptionEv(
    const QQmlSA::FixSuggestion *self) {
  return new QString(self->description());
}

//  bool QQmlSA::FixSuggestion::isAutoApplicable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlSA13FixSuggestion16isAutoApplicableEv(
    const QQmlSA::FixSuggestion *self) {
  return self->isAutoApplicable();
}

//  bool operator==(const FixSuggestion &lhs, const FixSuggestion &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSAeqERKNS_13FixSuggestionES2_(
    const QQmlSA::FixSuggestion *lhs,
    const QQmlSA::FixSuggestion *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const FixSuggestion &lhs, const FixSuggestion &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN6QQmlSAneERKNS_13FixSuggestionES2_(
    const QQmlSA::FixSuggestion *lhs,
    const QQmlSA::FixSuggestion *rhs) {
  return operator!=(*lhs, *rhs);
}
