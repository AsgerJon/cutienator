//  Written by dev_tooling.RitualGenerator from the records of QtGui/qfont.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qfont.h>
#include <QtCore/qbytearray.h>

//  QFont::Tag::Tag()
extern "C" Q_DECL_EXPORT
QFont::Tag *ritual_ZN5QFont3TagC1Ev() {
  return new QFont::Tag();
}

//  bool QFont::Tag::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QFont3Tag7isValidEv(const QFont::Tag *self) {
  return self->isValid();
}

//  quint32 QFont::Tag::value() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK5QFont3Tag5valueEv(const QFont::Tag *self) {
  return self->value();
}

//  QByteArray QFont::Tag::toString() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK5QFont3Tag8toStringEv(const QFont::Tag *self) {
  return new QByteArray(self->toString());
}

//  QFont::Tag::~Tag()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont3TagD1Ev(QFont::Tag *self) {
  delete self;
}
