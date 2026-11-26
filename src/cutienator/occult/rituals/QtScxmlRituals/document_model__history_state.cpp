//  Written by dev_tooling.RitualGenerator from the records of
//  QtScxml/6.12.0/QtScxml/private/qscxmlcompiler_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtScxml/6.12.0/QtScxml/private/qscxmlglobals_p.h>
#include <QtScxml/QtScxml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/6.12.0/QtScxml/private/qscxmlcompiler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtScxml/private/qscxmlcompiler_p.h>
#include <QtScxml/private/qscxmlexecutablecontent_p.h>
#include <QtCore/qxmlstream.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qfile.h>
#include <QtCore/qlist.h>
#include <QtCore/qstring.h>
#ifndef BUILD_QSCXMLC
#include <QtScxml/private/qscxmlinvokableservice_p.h>
#include <QtScxml/private/qscxmldatamodel_p.h>
#include <QtScxml/private/qscxmlstatemachine_p.h>
#include <QtScxml/qscxmlstatemachine.h>
#include <QtScxml/private/qscxmltabledata_p.h>
#include <QtCore/private/qmetaobjectbuilder_p.h>
#endif
#include <QtCore/qmap.h>
#include <functional>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from ../qtscxml/src/scxml/qscxmlcompiler.cpp, line 1144, as _ZN13DocumentModel4NodeD2Ev
inline DocumentModel::Node::~Node()
{
}

//  from ../qtscxml/src/scxml/qscxmlcompiler.cpp, line 1257, as _ZN13DocumentModel12HistoryState6acceptEPNS_11NodeVisitorE
inline void DocumentModel::HistoryState::accept(DocumentModel::NodeVisitor *visitor)
{
    if (visitor->visit(this)) {
        if (Transition *t = defaultConfiguration())
            t->accept(visitor);
    }
    visitor->endVisit(this);
}
//  -----------------------------------------------------------------------

//  A DocumentModel::HistoryState that Python can take functions over in. Every DocumentModel::HistoryState
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteDocumentModel_HistoryStateCall0)(const void *, DocumentModel::StateOrTransition *, int *);
typedef void * (*CuteDocumentModel_HistoryStateCall1)(const void *, int *);
typedef void (*CuteDocumentModel_HistoryStateCall2)(const void *, DocumentModel::NodeVisitor *, int *);
typedef void * (*CuteDocumentModel_HistoryStateCall3)(const void *, int *);
typedef void * (*CuteDocumentModel_HistoryStateCall4)(const void *, int *);
typedef void * (*CuteDocumentModel_HistoryStateCall5)(const void *, int *);
typedef void * (*CuteDocumentModel_HistoryStateCall6)(const void *, int *);
typedef void * (*CuteDocumentModel_HistoryStateCall7)(const void *, int *);
typedef void * (*CuteDocumentModel_HistoryStateCall8)(const void *, int *);
typedef void * (*CuteDocumentModel_HistoryStateCall9)(const void *, int *);
typedef void * (*CuteDocumentModel_HistoryStateCall10)(const void *, int *);
class CuteDocumentModel_HistoryState : public DocumentModel::HistoryState {
public:
  using DocumentModel::HistoryState::HistoryState;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13DocumentModel14StateContainer3addEPNS_17StateOrTransitionE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel4Node14asHistoryStateEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel4Node6acceptEPNS_11NodeVisitorE")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel4Node15asAbstractStateEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel4Node7asStateEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel4Node7asScxmlEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel4Node4asIfEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel4Node6asSendEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel4Node8asInvokeEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel4Node8asScriptEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel4Node12asTransitionEv")) {
      taken[10] = call;
      return true;
    }
    return false;
  }

  //  void DocumentModel::HistoryState::add(StateOrTransition *s)
  void add(DocumentModel::StateOrTransition *s) override {
    if (taken[0]) {
      int handled = 0;
      CuteDocumentModel_HistoryStateCall0 call = reinterpret_cast<CuteDocumentModel_HistoryStateCall0>(taken[0]);
      call(this, s, &handled);
      if (handled) return;
    }
    DocumentModel::HistoryState::add(s);
  }

  //  HistoryState *DocumentModel::HistoryState::asHistoryState()
  DocumentModel::HistoryState *asHistoryState() override {
    if (taken[1]) {
      int handled = 0;
      CuteDocumentModel_HistoryStateCall1 call = reinterpret_cast<CuteDocumentModel_HistoryStateCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::HistoryState *>(given);
    }
    return DocumentModel::HistoryState::asHistoryState();
  }

  //  void DocumentModel::HistoryState::accept(NodeVisitor *visitor)
  void accept(DocumentModel::NodeVisitor *visitor) override {
    if (taken[2]) {
      int handled = 0;
      CuteDocumentModel_HistoryStateCall2 call = reinterpret_cast<CuteDocumentModel_HistoryStateCall2>(taken[2]);
      call(this, visitor, &handled);
      if (handled) return;
    }
    DocumentModel::HistoryState::accept(visitor);
  }

  //  AbstractState *DocumentModel::AbstractState::asAbstractState()
  DocumentModel::AbstractState *asAbstractState() override {
    if (taken[3]) {
      int handled = 0;
      CuteDocumentModel_HistoryStateCall3 call = reinterpret_cast<CuteDocumentModel_HistoryStateCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::AbstractState *>(given);
    }
    return DocumentModel::AbstractState::asAbstractState();
  }

  //  State *DocumentModel::StateContainer::asState()
  DocumentModel::State *asState() override {
    if (taken[4]) {
      int handled = 0;
      CuteDocumentModel_HistoryStateCall4 call = reinterpret_cast<CuteDocumentModel_HistoryStateCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::State *>(given);
    }
    return DocumentModel::StateContainer::asState();
  }

  //  Scxml *DocumentModel::StateContainer::asScxml()
  DocumentModel::Scxml *asScxml() override {
    if (taken[5]) {
      int handled = 0;
      CuteDocumentModel_HistoryStateCall5 call = reinterpret_cast<CuteDocumentModel_HistoryStateCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::Scxml *>(given);
    }
    return DocumentModel::StateContainer::asScxml();
  }

  //  If *DocumentModel::Node::asIf()
  DocumentModel::If *asIf() override {
    if (taken[6]) {
      int handled = 0;
      CuteDocumentModel_HistoryStateCall6 call = reinterpret_cast<CuteDocumentModel_HistoryStateCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::If *>(given);
    }
    return DocumentModel::Node::asIf();
  }

  //  Send *DocumentModel::Node::asSend()
  DocumentModel::Send *asSend() override {
    if (taken[7]) {
      int handled = 0;
      CuteDocumentModel_HistoryStateCall7 call = reinterpret_cast<CuteDocumentModel_HistoryStateCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::Send *>(given);
    }
    return DocumentModel::Node::asSend();
  }

  //  Invoke *DocumentModel::Node::asInvoke()
  DocumentModel::Invoke *asInvoke() override {
    if (taken[8]) {
      int handled = 0;
      CuteDocumentModel_HistoryStateCall8 call = reinterpret_cast<CuteDocumentModel_HistoryStateCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::Invoke *>(given);
    }
    return DocumentModel::Node::asInvoke();
  }

  //  Script *DocumentModel::Node::asScript()
  DocumentModel::Script *asScript() override {
    if (taken[9]) {
      int handled = 0;
      CuteDocumentModel_HistoryStateCall9 call = reinterpret_cast<CuteDocumentModel_HistoryStateCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::Script *>(given);
    }
    return DocumentModel::Node::asScript();
  }

  //  Transition *DocumentModel::Node::asTransition()
  DocumentModel::Transition *asTransition() override {
    if (taken[10]) {
      int handled = 0;
      CuteDocumentModel_HistoryStateCall10 call = reinterpret_cast<CuteDocumentModel_HistoryStateCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::Transition *>(given);
    }
    return DocumentModel::Node::asTransition();
  }
};

//  DocumentModel::HistoryState::HistoryState(const XmlLocation &xmlLocation)
extern "C" Q_DECL_EXPORT
DocumentModel::HistoryState *ritual_ZN13DocumentModel12HistoryStateC1ERKNS_11XmlLocationE(
    const DocumentModel::XmlLocation *xmlLocation) {
  return new CuteDocumentModel_HistoryState(*xmlLocation);
}

//  void DocumentModel::HistoryState::add(StateOrTransition *s)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DocumentModel12HistoryState3addEPNS_17StateOrTransitionE(
    DocumentModel::HistoryState *self,
    DocumentModel::StateOrTransition *s) {
  self->add(s);
}

//  Transition *DocumentModel::HistoryState::defaultConfiguration()
extern "C" Q_DECL_EXPORT
DocumentModel::Transition *ritual_ZN13DocumentModel12HistoryState20defaultConfigurationEv(
    DocumentModel::HistoryState *self) {
  return self->defaultConfiguration();
}

//  HistoryState *DocumentModel::HistoryState::asHistoryState()
extern "C" Q_DECL_EXPORT
DocumentModel::HistoryState *ritual_ZN13DocumentModel12HistoryState14asHistoryStateEv(
    DocumentModel::HistoryState *self) {
  return self->asHistoryState();
}

//  void DocumentModel::HistoryState::accept(NodeVisitor *visitor)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DocumentModel12HistoryState6acceptEPNS_11NodeVisitorE(
    DocumentModel::HistoryState *self,
    DocumentModel::NodeVisitor *visitor) {
  self->accept(visitor);
}

//  DocumentModel::HistoryState as the DocumentModel::StateOrTransition it is
//      built on
extern "C" Q_DECL_EXPORT
DocumentModel::StateOrTransition *ritual_cast_DocumentModel_HistoryState_DocumentModel_StateOrTransition(
    DocumentModel::HistoryState *self) {
  return static_cast<DocumentModel::StateOrTransition *>(self);
}

//  a Python function taken by a CuteDocumentModel_HistoryState, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_DocumentModel_HistoryState(
    DocumentModel::HistoryState *self,
    const char *key,
    void *call) {
  return static_cast<CuteDocumentModel_HistoryState *>(self)->take(key, call);
}

//  void DocumentModel::HistoryState::add(StateOrTransition *s)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13DocumentModel12HistoryState3addEPNS_17StateOrTransitionE(
    DocumentModel::HistoryState *self,
    DocumentModel::StateOrTransition *s) {
  self->DocumentModel::HistoryState::add(s);
}

//  HistoryState *DocumentModel::HistoryState::asHistoryState()
extern "C" Q_DECL_EXPORT
DocumentModel::HistoryState *ritual_own_ZN13DocumentModel12HistoryState14asHistoryStateEv(
    DocumentModel::HistoryState *self) {
  return self->DocumentModel::HistoryState::asHistoryState();
}

//  void DocumentModel::HistoryState::accept(NodeVisitor *visitor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13DocumentModel12HistoryState6acceptEPNS_11NodeVisitorE(
    DocumentModel::HistoryState *self,
    DocumentModel::NodeVisitor *visitor) {
  self->DocumentModel::HistoryState::accept(visitor);
}
