//  Written by hand on 2026-11-25 from
//  QtAxServer/qaxaggregated.h, Qt 6.12.0, from Qt's source. Kept as
//  it is when the generator runs again.
//  Qt builds ActiveQt for Windows only. AxServer is a static library,
//  all of it compiled into ours, so the class is taken as exported.
//  The 'long' of 'queryInterface' is an 'HRESULT' of Windows.
//  Not written: the constructor, as the class is abstract
//  ('queryInterface' is pure), and the macro 'QAXAGG_IUNKNOWN'.
#include <QtCore/qglobal.h>
#if defined(Q_OS_WIN)
#include <QtAxServer/qaxaggregated.h>
#include <QtCore/quuid.h>
#include <QtWidgets/qwidget.h>
#include <cstring>

//  A QAxAggregated that Python can take functions over in. Every
//  QAxAggregated Python makes is one. Each function below asks the
//  Python function handed over for it, and runs Qt's own without
//  one.
typedef long (*CuteQAxAggregatedCall0)(const void *, const QUuid *, void **, int *);
class CuteQAxAggregated : public QAxAggregated {
public:
  using QAxAggregated::QAxAggregated;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13QAxAggregated14queryInterfaceERK5QUuidPPv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  long QAxAggregated::queryInterface(const QUuid &iid, void **iface)
  long queryInterface(const QUuid &iid, void **iface) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAxAggregatedCall0 call = reinterpret_cast<CuteQAxAggregatedCall0>(taken[0]);
      long given = call(this, &iid, iface, &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  QAxAggregated::~QAxAggregated()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QAxAggregatedD1Ev(QAxAggregated *self) {
  delete self;
}

//  long QAxAggregated::queryInterface(const QUuid &iid, void **iface)
extern "C" Q_DECL_EXPORT
long ritual_ZN13QAxAggregated14queryInterfaceERK5QUuidPPv(
    QAxAggregated *self,
    const QUuid *iid,
    void **iface) {
  return self->queryInterface(*iid, iface);
}

//  IUnknown *QAxAggregated::controllingUnknown() const
extern "C" Q_DECL_EXPORT
IUnknown *ritual_ZNK13QAxAggregated18controllingUnknownEv(
    const QAxAggregated *self) {
  return self->controllingUnknown();
}

//  QWidget *QAxAggregated::widget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK13QAxAggregated6widgetEv(const QAxAggregated *self) {
  return self->widget();
}

//  QObject *QAxAggregated::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK13QAxAggregated6objectEv(const QAxAggregated *self) {
  return self->object();
}

//  a Python function taken by a CuteQAxAggregated, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAxAggregated(
    QAxAggregated *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAxAggregated *>(self)->take(key, call);
}

#endif  // defined(Q_OS_WIN)
