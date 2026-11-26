//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qcssparser_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(cssparser)
#if !defined(QT_NO_CSSPARSER)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qcssparser_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  int QCss::Selector::specificity() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK4QCss8Selector11specificityEv(const QCss::Selector *self) {
  return self->specificity();
}

//  quint64 QCss::Selector::pseudoClass(quint64 *negated) const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK4QCss8Selector11pseudoClassEPy(
    const QCss::Selector *self,
    quint64 *negated) {
  return self->pseudoClass(negated);
}

//  QString QCss::Selector::pseudoElement() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK4QCss8Selector13pseudoElementEv(
    const QCss::Selector *self) {
  return new QString(self->pseudoElement());
}

//  QCss::Selector::~Selector()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QCss8SelectorD1Ev(QCss::Selector *self) {
  delete self;
}

#endif  // !defined(QT_NO_CSSPARSER)
#endif  // QT_CONFIG(cssparser)
