//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qmdiarea_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(mdiarea)
#if QT_CONFIG(mdiarea)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qmdiarea_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QMdi::Rearranger that Python can take functions over in. Every QMdi::Rearranger
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(mdiarea)
typedef int (*CuteQMdi_RearrangerCall0)(const void *, int *);
#endif  // QT_CONFIG(mdiarea)
class CuteQMdi_Rearranger : public QMdi::Rearranger {
public:
  using QMdi::Rearranger::Rearranger;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(mdiarea)
    if (!std::strcmp(key, "_ZNK4QMdi10Rearranger4typeEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(mdiarea)
    return false;
  }

#if QT_CONFIG(mdiarea)
  //  Type QMdi::Rearranger::type() const
  QMdi::Rearranger::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQMdi_RearrangerCall0 call = reinterpret_cast<CuteQMdi_RearrangerCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QMdi::Rearranger::Type>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(mdiarea)
};

//  Type QMdi::Rearranger::type() const
extern "C" Q_DECL_EXPORT
QMdi::Rearranger::Type ritual_ZNK4QMdi10Rearranger4typeEv(
    const QMdi::Rearranger *self) {
  return self->type();
}

//  QMdi::Rearranger::~Rearranger()
extern "C" Q_DECL_EXPORT
void ritual_ZN4QMdi10RearrangerD1Ev(QMdi::Rearranger *self) {
  delete self;
}

//  a Python function taken by a CuteQMdi_Rearranger, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMdi_Rearranger(
    QMdi::Rearranger *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMdi_Rearranger *>(self)->take(key, call);
}

#endif  // QT_CONFIG(mdiarea)
#endif  // QT_CONFIG(mdiarea)
