//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtextobject.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtextobject.h>
#include <QtGui/qtextformat.h>
#include <QtCore/qstring.h>

//  QTextFragment::QTextFragment()
extern "C" Q_DECL_EXPORT
QTextFragment *ritual_ZN13QTextFragmentC1Ev() {
  return new QTextFragment();
}

//  QTextFragment::QTextFragment(const QTextFragment &o)
extern "C" Q_DECL_EXPORT
QTextFragment *ritual_ZN13QTextFragmentC1ERKS_(const QTextFragment *o) {
  return new QTextFragment(*o);
}

//  bool QTextFragment::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QTextFragment7isValidEv(const QTextFragment *self) {
  return self->isValid();
}

//  bool QTextFragment::operator==(const QTextFragment &o) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QTextFragmenteqERKS_(
    const QTextFragment *self,
    const QTextFragment *o) {
  return self->operator==(*o);
}

//  bool QTextFragment::operator!=(const QTextFragment &o) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QTextFragmentneERKS_(
    const QTextFragment *self,
    const QTextFragment *o) {
  return self->operator!=(*o);
}

//  bool QTextFragment::operator<(const QTextFragment &o) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QTextFragmentltERKS_(
    const QTextFragment *self,
    const QTextFragment *o) {
  return self->operator<(*o);
}

//  int QTextFragment::position() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QTextFragment8positionEv(const QTextFragment *self) {
  return self->position();
}

//  int QTextFragment::length() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QTextFragment6lengthEv(const QTextFragment *self) {
  return self->length();
}

//  bool QTextFragment::contains(int position) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QTextFragment8containsEi(
    const QTextFragment *self,
    int position) {
  return self->contains(position);
}

//  QTextCharFormat QTextFragment::charFormat() const
extern "C" Q_DECL_EXPORT
QTextCharFormat *ritual_ZNK13QTextFragment10charFormatEv(
    const QTextFragment *self) {
  return new QTextCharFormat(self->charFormat());
}

//  int QTextFragment::charFormatIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QTextFragment15charFormatIndexEv(const QTextFragment *self) {
  return self->charFormatIndex();
}

//  QString QTextFragment::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QTextFragment4textEv(const QTextFragment *self) {
  return new QString(self->text());
}

//  QTextFragment::~QTextFragment()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QTextFragmentD1Ev(QTextFragment *self) {
  delete self;
}
