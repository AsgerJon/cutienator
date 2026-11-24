//  Written by dev_tooling.RitualGenerator from the records of QtDataVisualiz
//  ation/6.12.0/QtDataVisualization/private/abstractdeclarativeinterface_p.h
//  , Qt 6.12.0. Changes made here are lost.
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/datavisualizationglobal_p.h>
#include <QtDataVisualization/QtDataVisualization>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDataVisualization/6.12.0/QtDataVisualization/private/abstractdeclarativeinterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A AbstractDeclarativeInterface that Python can take functions over in. Every AbstractDeclarativeInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteAbstractDeclarativeInterfaceCall0)(const void *, int *);
class CuteAbstractDeclarativeInterface : public AbstractDeclarativeInterface {
public:
  using AbstractDeclarativeInterface::AbstractDeclarativeInterface;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK28AbstractDeclarativeInterface7isReadyEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  bool AbstractDeclarativeInterface::isReady() const
  bool isReady() const override {
    if (taken[0]) {
      int handled = 0;
      CuteAbstractDeclarativeInterfaceCall0 call = reinterpret_cast<CuteAbstractDeclarativeInterfaceCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  AbstractDeclarativeInterface::~AbstractDeclarativeInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN28AbstractDeclarativeInterfaceD1Ev(
    AbstractDeclarativeInterface *self) {
  delete self;
}

//  bool AbstractDeclarativeInterface::isReady() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28AbstractDeclarativeInterface7isReadyEv(
    const AbstractDeclarativeInterface *self) {
  return self->isReady();
}

//  a Python function taken by a CuteAbstractDeclarativeInterface, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_AbstractDeclarativeInterface(
    AbstractDeclarativeInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteAbstractDeclarativeInterface *>(self)->take(key, call);
}
