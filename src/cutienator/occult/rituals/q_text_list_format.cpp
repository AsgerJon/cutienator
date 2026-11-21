//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtextformat.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtextformat.h>
#include <QtCore/qstring.h>

//  QTextListFormat::QTextListFormat()
extern "C" Q_DECL_EXPORT
QTextListFormat *ritual_ZN15QTextListFormatC1Ev() {
  return new QTextListFormat();
}

//  bool QTextListFormat::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QTextListFormat7isValidEv(const QTextListFormat *self) {
  return self->isValid();
}

//  void QTextListFormat::setStyle(Style style)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextListFormat8setStyleENS_5StyleE(
    QTextListFormat *self,
    QTextListFormat::Style style) {
  self->setStyle(style);
}

//  Style QTextListFormat::style() const
extern "C" Q_DECL_EXPORT
QTextListFormat::Style ritual_ZNK15QTextListFormat5styleEv(
    const QTextListFormat *self) {
  return self->style();
}

//  void QTextListFormat::setIndent(int indent)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextListFormat9setIndentEi(
    QTextListFormat *self,
    int indent) {
  self->setIndent(indent);
}

//  int QTextListFormat::indent() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QTextListFormat6indentEv(const QTextListFormat *self) {
  return self->indent();
}

//  void QTextListFormat::setNumberPrefix(const QString &numberPrefix)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextListFormat15setNumberPrefixERK7QString(
    QTextListFormat *self,
    const QString *numberPrefix) {
  self->setNumberPrefix(*numberPrefix);
}

//  QString QTextListFormat::numberPrefix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QTextListFormat12numberPrefixEv(
    const QTextListFormat *self) {
  return new QString(self->numberPrefix());
}

//  void QTextListFormat::setNumberSuffix(const QString &numberSuffix)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextListFormat15setNumberSuffixERK7QString(
    QTextListFormat *self,
    const QString *numberSuffix) {
  self->setNumberSuffix(*numberSuffix);
}

//  QString QTextListFormat::numberSuffix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QTextListFormat12numberSuffixEv(
    const QTextListFormat *self) {
  return new QString(self->numberSuffix());
}

//  void QTextListFormat::setStart(int indent)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextListFormat8setStartEi(
    QTextListFormat *self,
    int indent) {
  self->setStart(indent);
}

//  int QTextListFormat::start() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QTextListFormat5startEv(const QTextListFormat *self) {
  return self->start();
}

//  QTextListFormat::~QTextListFormat()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextListFormatD1Ev(QTextListFormat *self) {
  delete self;
}
