//  Written by dev_tooling.RitualGenerator from the records of QtXml/qdom.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtXml/qtxmlglobal.h>
#if QT_CONFIG(dom)
#if QT_CONFIG(dom)
#include <QtXml/qdom.h>

//  bool QDomDocument::ParseResult::operator bool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QDomDocument11ParseResultcvbEv(
    const QDomDocument::ParseResult *self) {
  return self->operator bool();
}

//  QDomDocument::ParseResult::~ParseResult()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDomDocument11ParseResultD1Ev(
    QDomDocument::ParseResult *self) {
  delete self;
}

#endif  // QT_CONFIG(dom)
#endif  // QT_CONFIG(dom)
