//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qtparsecommon_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qtparsecommon_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>

//  bool QtParseCommon::ParsedText::operator bool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QtParseCommon10ParsedTextcvbEv(
    const QtParseCommon::ParsedText *self) {
  return self->operator bool();
}

//  bool QtParseCommon::ParsedText::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QtParseCommon10ParsedText7isEmptyEv(
    const QtParseCommon::ParsedText *self) {
  return self->isEmpty();
}

//  qsizetype QtParseCommon::ParsedText::size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK13QtParseCommon10ParsedText4sizeEv(
    const QtParseCommon::ParsedText *self) {
  return self->size();
}

//  QStringView QtParseCommon::ParsedText::used(QStringView text) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QtParseCommon10ParsedText4usedE11QStringView(
    const QtParseCommon::ParsedText *self,
    const QString *text) {
  return new QString(self->used(QStringView(*text)).toString());
}

//  QtParseCommon::ParsedText::~ParsedText()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QtParseCommon10ParsedTextD1Ev(
    QtParseCommon::ParsedText *self) {
  delete self;
}
