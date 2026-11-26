//  Written by dev_tooling.RitualGenerator from the records of QtGui/qfont.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qfont.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qdebug.h>
#include <optional>
#include <QtGui/QFont>
#include <QtCore/QAnyStringView>

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

//  std::optional<Tag> QFont::Tag::fromValue(quint32 value)
extern "C" Q_DECL_EXPORT
std::optional<QFont::Tag> *ritual_ZN5QFont3Tag9fromValueEj(quint32 value) {
  return new std::optional<QFont::Tag>(QFont::Tag::fromValue(value));
}

//  std::optional<Tag> QFont::Tag::fromString(QAnyStringView view)
extern "C" Q_DECL_EXPORT
std::optional<QFont::Tag> *ritual_ZN5QFont3Tag10fromStringE14QAnyStringView(
    const QString *view) {
  return new std::optional<QFont::Tag>(
      QFont::Tag::fromString(
          QAnyStringView(*view)));
}

#if !defined(QT_NO_DATASTREAM)
//  QDataStream &operator<<(QDataStream &a0, Tag a1)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZlsR11QDataStreamN5QFont3TagE(
    QDataStream *a0,
    const QFont::Tag *a1) {
  return &(operator<<(*a0, *a1));
}
#endif  // !defined(QT_NO_DATASTREAM)

#if !defined(QT_NO_DATASTREAM)
//  QDataStream &operator>>(QDataStream &a0, Tag &a1)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZrsR11QDataStreamRN5QFont3TagE(
    QDataStream *a0,
    QFont::Tag *a1) {
  return &(operator>>(*a0, *a1));
}
#endif  // !defined(QT_NO_DATASTREAM)

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug debug, Tag tag)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugN5QFont3TagE(
    const QDebug *debug,
    const QFont::Tag *tag) {
  return new QDebug(operator<<(*debug, *tag));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  bool operator==(const QFont::Tag &lhs, const QFont::Tag &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKN5QFont3TagES2_(
    const QFont::Tag *lhs,
    const QFont::Tag *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QFont::Tag &lhs, const QFont::Tag &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKN5QFont3TagES2_(
    const QFont::Tag *lhs,
    const QFont::Tag *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QFont::Tag &lhs, const QFont::Tag &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKN5QFont3TagES2_(
    const QFont::Tag *lhs,
    const QFont::Tag *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const QFont::Tag &lhs, const QFont::Tag &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKN5QFont3TagES2_(
    const QFont::Tag *lhs,
    const QFont::Tag *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const QFont::Tag &lhs, const QFont::Tag &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKN5QFont3TagES2_(
    const QFont::Tag *lhs,
    const QFont::Tag *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const QFont::Tag &lhs, const QFont::Tag &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKN5QFont3TagES2_(
    const QFont::Tag *lhs,
    const QFont::Tag *rhs) {
  return operator>=(*lhs, *rhs);
}

//  QFont::Tag::~Tag()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QFont3TagD1Ev(QFont::Tag *self) {
  delete self;
}

//  a std::optional<QFont::Tag> a ritual of QFont::Tag gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QFont_Tag__std_optional_QFont_Tag(
    std::optional<QFont::Tag> *self) {
  delete self;
}
