//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlcompiler_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlcompiler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A DocumentModel::AbstractState that Python can take functions over in. Every DocumentModel::AbstractState
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteDocumentModel_AbstractStateCall0)(const void *, int *);
typedef void (*CuteDocumentModel_AbstractStateCall1)(const void *, DocumentModel::StateOrTransition *, int *);
typedef void * (*CuteDocumentModel_AbstractStateCall2)(const void *, int *);
typedef void * (*CuteDocumentModel_AbstractStateCall3)(const void *, int *);
class CuteDocumentModel_AbstractState : public DocumentModel::AbstractState {
public:
  using DocumentModel::AbstractState::AbstractState;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13DocumentModel14StateContainer15asAbstractStateEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel14StateContainer3addEPNS_17StateOrTransitionE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel14StateContainer7asStateEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel14StateContainer7asScxmlEv")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  AbstractState *DocumentModel::AbstractState::asAbstractState()
  DocumentModel::AbstractState *asAbstractState() override {
    if (taken[0]) {
      int handled = 0;
      CuteDocumentModel_AbstractStateCall0 call = reinterpret_cast<CuteDocumentModel_AbstractStateCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::AbstractState *>(given);
    }
    return DocumentModel::AbstractState::asAbstractState();
  }

  //  void DocumentModel::StateContainer::add(StateOrTransition *s)
  void add(DocumentModel::StateOrTransition *s) override {
    if (taken[1]) {
      int handled = 0;
      CuteDocumentModel_AbstractStateCall1 call = reinterpret_cast<CuteDocumentModel_AbstractStateCall1>(taken[1]);
      call(this, s, &handled);
      if (handled) return;
    }
  }

  //  State *DocumentModel::StateContainer::asState()
  DocumentModel::State *asState() override {
    if (taken[2]) {
      int handled = 0;
      CuteDocumentModel_AbstractStateCall2 call = reinterpret_cast<CuteDocumentModel_AbstractStateCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::State *>(given);
    }
    return DocumentModel::StateContainer::asState();
  }

  //  Scxml *DocumentModel::StateContainer::asScxml()
  DocumentModel::Scxml *asScxml() override {
    if (taken[3]) {
      int handled = 0;
      CuteDocumentModel_AbstractStateCall3 call = reinterpret_cast<CuteDocumentModel_AbstractStateCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::Scxml *>(given);
    }
    return DocumentModel::StateContainer::asScxml();
  }
};

//  AbstractState *DocumentModel::AbstractState::asAbstractState()
extern "C" Q_DECL_EXPORT
DocumentModel::AbstractState *ritual_ZN13DocumentModel13AbstractState15asAbstractStateEv(
    DocumentModel::AbstractState *self) {
  return self->asAbstractState();
}

//  a Python function taken by a CuteDocumentModel_AbstractState, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_DocumentModel_AbstractState(
    DocumentModel::AbstractState *self,
    const char *key,
    void *call) {
  return static_cast<CuteDocumentModel_AbstractState *>(self)->take(key, call);
}

//  AbstractState *DocumentModel::AbstractState::asAbstractState()
extern "C" Q_DECL_EXPORT
DocumentModel::AbstractState *ritual_own_ZN13DocumentModel13AbstractState15asAbstractStateEv(
    DocumentModel::AbstractState *self) {
  return self->DocumentModel::AbstractState::asAbstractState();
}
