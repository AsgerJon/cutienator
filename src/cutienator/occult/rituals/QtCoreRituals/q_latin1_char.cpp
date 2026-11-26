//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qchar.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qchar.h>

//  QLatin1Char::QLatin1Char(char c)
extern "C" Q_DECL_EXPORT
QLatin1Char *ritual_ZN11QLatin1CharC1Ec(char c) {
  return new QLatin1Char(c);
}

//  char QLatin1Char::toLatin1() const
extern "C" Q_DECL_EXPORT
char ritual_ZNK11QLatin1Char8toLatin1Ev(const QLatin1Char *self) {
  return self->toLatin1();
}

//  char16_t QLatin1Char::unicode() const
extern "C" Q_DECL_EXPORT
char16_t ritual_ZNK11QLatin1Char7unicodeEv(const QLatin1Char *self) {
  return self->unicode();
}

//  bool operator==(const QLatin1Char &lhs, const QLatin1Char &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK11QLatin1CharS1_(
    const QLatin1Char *lhs,
    const QLatin1Char *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QLatin1Char &lhs, const QLatin1Char &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK11QLatin1CharS1_(
    const QLatin1Char *lhs,
    const QLatin1Char *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QLatin1Char &lhs, const QLatin1Char &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK11QLatin1CharS1_(
    const QLatin1Char *lhs,
    const QLatin1Char *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const QLatin1Char &lhs, const QLatin1Char &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK11QLatin1CharS1_(
    const QLatin1Char *lhs,
    const QLatin1Char *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const QLatin1Char &lhs, const QLatin1Char &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK11QLatin1CharS1_(
    const QLatin1Char *lhs,
    const QLatin1Char *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const QLatin1Char &lhs, const QLatin1Char &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK11QLatin1CharS1_(
    const QLatin1Char *lhs,
    const QLatin1Char *rhs) {
  return operator>=(*lhs, *rhs);
}

//  bool operator==(const QLatin1Char &lhs, const char &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK11QLatin1CharRKc(const QLatin1Char *lhs, char rhs) {
  return operator==(*lhs, rhs);
}

//  bool operator!=(const QLatin1Char &lhs, const char &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK11QLatin1CharRKc(const QLatin1Char *lhs, char rhs) {
  return operator!=(*lhs, rhs);
}

//  bool operator<(const QLatin1Char &lhs, const char &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK11QLatin1CharRKc(const QLatin1Char *lhs, char rhs) {
  return operator<(*lhs, rhs);
}

//  bool operator>(const QLatin1Char &lhs, const char &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK11QLatin1CharRKc(const QLatin1Char *lhs, char rhs) {
  return operator>(*lhs, rhs);
}

//  bool operator<=(const QLatin1Char &lhs, const char &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK11QLatin1CharRKc(const QLatin1Char *lhs, char rhs) {
  return operator<=(*lhs, rhs);
}

//  bool operator>=(const QLatin1Char &lhs, const char &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK11QLatin1CharRKc(const QLatin1Char *lhs, char rhs) {
  return operator>=(*lhs, rhs);
}

//  bool operator==(const char &lhs, const QLatin1Char &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRKcRK11QLatin1Char(char lhs, const QLatin1Char *rhs) {
  return operator==(lhs, *rhs);
}

//  bool operator!=(const char &lhs, const QLatin1Char &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRKcRK11QLatin1Char(char lhs, const QLatin1Char *rhs) {
  return operator!=(lhs, *rhs);
}

//  bool operator<(const char &lhs, const QLatin1Char &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRKcRK11QLatin1Char(char lhs, const QLatin1Char *rhs) {
  return operator<(lhs, *rhs);
}

//  bool operator>(const char &lhs, const QLatin1Char &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRKcRK11QLatin1Char(char lhs, const QLatin1Char *rhs) {
  return operator>(lhs, *rhs);
}

//  bool operator<=(const char &lhs, const QLatin1Char &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRKcRK11QLatin1Char(char lhs, const QLatin1Char *rhs) {
  return operator<=(lhs, *rhs);
}

//  bool operator>=(const char &lhs, const QLatin1Char &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRKcRK11QLatin1Char(char lhs, const QLatin1Char *rhs) {
  return operator>=(lhs, *rhs);
}

//  char16_t QLatin1Char::operator char16_t() const
extern "C" Q_DECL_EXPORT
char16_t ritual_ZNK11QLatin1CharcvDsEv(const QLatin1Char *self) {
  return self->operator char16_t();
}

//  QLatin1Char::~QLatin1Char()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLatin1CharD1Ev(QLatin1Char *self) {
  delete self;
}
