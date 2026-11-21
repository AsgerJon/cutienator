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

//  QLatin1Char::~QLatin1Char()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QLatin1CharD1Ev(QLatin1Char *self) {
  delete self;
}
