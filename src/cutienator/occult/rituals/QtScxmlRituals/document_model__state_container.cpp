//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlcompiler_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlcompiler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A DocumentModel::StateContainer that Python can take functions over in. Every DocumentModel::StateContainer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteDocumentModel_StateContainerCall0)(const void *, DocumentModel::StateOrTransition *, int *);
typedef void * (*CuteDocumentModel_StateContainerCall1)(const void *, int *);
typedef void * (*CuteDocumentModel_StateContainerCall2)(const void *, int *);
typedef void * (*CuteDocumentModel_StateContainerCall3)(const void *, int *);
class CuteDocumentModel_StateContainer : public DocumentModel::StateContainer {
public:
  using DocumentModel::StateContainer::StateContainer;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13DocumentModel14StateContainer3addEPNS_17StateOrTransitionE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel14StateContainer15asAbstractStateEv")) {
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

  //  void DocumentModel::StateContainer::add(StateOrTransition *s)
  void add(DocumentModel::StateOrTransition *s) override {
    if (taken[0]) {
      int handled = 0;
      CuteDocumentModel_StateContainerCall0 call = reinterpret_cast<CuteDocumentModel_StateContainerCall0>(taken[0]);
      call(this, s, &handled);
      if (handled) return;
    }
  }

  //  AbstractState *DocumentModel::StateContainer::asAbstractState()
  DocumentModel::AbstractState *asAbstractState() override {
    if (taken[1]) {
      int handled = 0;
      CuteDocumentModel_StateContainerCall1 call = reinterpret_cast<CuteDocumentModel_StateContainerCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::AbstractState *>(given);
    }
    return DocumentModel::StateContainer::asAbstractState();
  }

  //  State *DocumentModel::StateContainer::asState()
  DocumentModel::State *asState() override {
    if (taken[2]) {
      int handled = 0;
      CuteDocumentModel_StateContainerCall2 call = reinterpret_cast<CuteDocumentModel_StateContainerCall2>(taken[2]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::State *>(given);
    }
    return DocumentModel::StateContainer::asState();
  }

  //  Scxml *DocumentModel::StateContainer::asScxml()
  DocumentModel::Scxml *asScxml() override {
    if (taken[3]) {
      int handled = 0;
      CuteDocumentModel_StateContainerCall3 call = reinterpret_cast<CuteDocumentModel_StateContainerCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::Scxml *>(given);
    }
    return DocumentModel::StateContainer::asScxml();
  }
};

//  DocumentModel::StateContainer::StateContainer()
extern "C" Q_DECL_EXPORT
DocumentModel::StateContainer *ritual_ZN13DocumentModel14StateContainerC1Ev() {
  return new CuteDocumentModel_StateContainer();
}

//  DocumentModel::StateContainer::~StateContainer()
extern "C" Q_DECL_EXPORT
void ritual_ZN13DocumentModel14StateContainerD1Ev(
    DocumentModel::StateContainer *self) {
  delete self;
}

//  void DocumentModel::StateContainer::add(StateOrTransition *s)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DocumentModel14StateContainer3addEPNS_17StateOrTransitionE(
    DocumentModel::StateContainer *self,
    DocumentModel::StateOrTransition *s) {
  self->add(s);
}

//  AbstractState *DocumentModel::StateContainer::asAbstractState()
extern "C" Q_DECL_EXPORT
DocumentModel::AbstractState *ritual_ZN13DocumentModel14StateContainer15asAbstractStateEv(
    DocumentModel::StateContainer *self) {
  return self->asAbstractState();
}

//  State *DocumentModel::StateContainer::asState()
extern "C" Q_DECL_EXPORT
DocumentModel::State *ritual_ZN13DocumentModel14StateContainer7asStateEv(
    DocumentModel::StateContainer *self) {
  return self->asState();
}

//  Scxml *DocumentModel::StateContainer::asScxml()
extern "C" Q_DECL_EXPORT
DocumentModel::Scxml *ritual_ZN13DocumentModel14StateContainer7asScxmlEv(
    DocumentModel::StateContainer *self) {
  return self->asScxml();
}

//  a Python function taken by a CuteDocumentModel_StateContainer, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_DocumentModel_StateContainer(
    DocumentModel::StateContainer *self,
    const char *key,
    void *call) {
  return static_cast<CuteDocumentModel_StateContainer *>(self)->take(key, call);
}

//  AbstractState *DocumentModel::StateContainer::asAbstractState()
extern "C" Q_DECL_EXPORT
DocumentModel::AbstractState *ritual_own_ZN13DocumentModel14StateContainer15asAbstractStateEv(
    DocumentModel::StateContainer *self) {
  return self->DocumentModel::StateContainer::asAbstractState();
}

//  State *DocumentModel::StateContainer::asState()
extern "C" Q_DECL_EXPORT
DocumentModel::State *ritual_own_ZN13DocumentModel14StateContainer7asStateEv(
    DocumentModel::StateContainer *self) {
  return self->DocumentModel::StateContainer::asState();
}

//  Scxml *DocumentModel::StateContainer::asScxml()
extern "C" Q_DECL_EXPORT
DocumentModel::Scxml *ritual_own_ZN13DocumentModel14StateContainer7asScxmlEv(
    DocumentModel::StateContainer *self) {
  return self->DocumentModel::StateContainer::asScxml();
}
