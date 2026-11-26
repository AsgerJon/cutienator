//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/q20functional.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by
//  hand, instances of templates of the class: 5. Kept as it is when the
//  generator runs again.
#include <QtCore/qglobal.h>
#if !(defined(__cpp_lib_ranges))
#include <QtCore/q20functional.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>

//  q20::identity::~identity()
extern "C" Q_DECL_EXPORT
void ritual_ZN3q208identityD1Ev(q20::identity *self) {
  delete self;
}

//  int &q20::identity::operator()<int &>(int &t) const
extern "C" Q_DECL_EXPORT
int * ritual_ZNK3q208identityclIRiEEOT_S4_(
    const q20::identity *self,
    int *t) {
  return &(self->operator()<int &>(*t));
}

//  double &q20::identity::operator()<double &>(double &t) const
extern "C" Q_DECL_EXPORT
double * ritual_ZNK3q208identityclIRdEEOT_S4_(
    const q20::identity *self,
    double *t) {
  return &(self->operator()<double &>(*t));
}

//  bool &q20::identity::operator()<bool &>(bool &t) const
extern "C" Q_DECL_EXPORT
bool * ritual_ZNK3q208identityclIRbEEOT_S4_(
    const q20::identity *self,
    bool *t) {
  return &(self->operator()<bool &>(*t));
}

//  QString &q20::identity::operator()<QString &>(QString &t) const
extern "C" Q_DECL_EXPORT
QString * ritual_ZNK3q208identityclIR7QStringEEOT_S5_(
    const q20::identity *self,
    QString *t) {
  return &(self->operator()<QString &>(*t));
}

//  QVariant &q20::identity::operator()<QVariant &>(QVariant &t) const
extern "C" Q_DECL_EXPORT
QVariant * ritual_ZNK3q208identityclIR8QVariantEEOT_S5_(
    const q20::identity *self,
    QVariant *t) {
  return &(self->operator()<QVariant &>(*t));
}

#endif  // !(defined(__cpp_lib_ranges))
