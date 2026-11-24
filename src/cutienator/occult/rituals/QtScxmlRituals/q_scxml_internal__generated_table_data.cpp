//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmltabledata_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmltabledata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QScxmlInternal::GeneratedTableData that Python can take functions over in. Every QScxmlInternal::GeneratedTableData
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQScxmlInternal_GeneratedTableDataCall0)(const void *, int, int *);
class CuteQScxmlInternal_GeneratedTableData : public QScxmlInternal::GeneratedTableData {
public:
  using QScxmlInternal::GeneratedTableData::GeneratedTableData;
  CuteQScxmlInternal_GeneratedTableData(const QScxmlInternal::GeneratedTableData &other) : QScxmlInternal::GeneratedTableData(other) {}
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK15QScxmlTableData14serviceFactoryEi")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  QScxmlInvokableServiceFactory
  //      *QScxmlInternal::GeneratedTableData::serviceFactory(int id) const
  QScxmlInvokableServiceFactory *serviceFactory(int id) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQScxmlInternal_GeneratedTableDataCall0 call = reinterpret_cast<CuteQScxmlInternal_GeneratedTableDataCall0>(taken[0]);
      void * given = call(this, id, &handled);
      if (handled) return static_cast<QScxmlInvokableServiceFactory *>(given);
    }
    return QScxmlInternal::GeneratedTableData::serviceFactory(id);
  }
};

//  QScxmlInternal::GeneratedTableData::~GeneratedTableData()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QScxmlInternal18GeneratedTableDataD1Ev(
    QScxmlInternal::GeneratedTableData *self) {
  delete self;
}

//  a Python function taken by a CuteQScxmlInternal_GeneratedTableData, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QScxmlInternal_GeneratedTableData(
    QScxmlInternal::GeneratedTableData *self,
    const char *key,
    void *call) {
  return static_cast<CuteQScxmlInternal_GeneratedTableData *>(self)->take(key, call);
}

//  QScxmlInvokableServiceFactory
//      *QScxmlInternal::GeneratedTableData::serviceFactory(int id) const
extern "C" Q_DECL_EXPORT
QScxmlInvokableServiceFactory *ritual_own_ZNK14QScxmlInternal18GeneratedTableData14serviceFactoryEi(
    const QScxmlInternal::GeneratedTableData *self,
    int id) {
  return self->QScxmlInternal::GeneratedTableData::serviceFactory(id);
}
