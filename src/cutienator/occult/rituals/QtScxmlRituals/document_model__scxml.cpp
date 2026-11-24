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
#include "qscxmlcompiler_p.h"
#include "qscxmlexecutablecontent_p.h"
#include <qxmlstream.h>
#include <qloggingcategory.h>
#include <qfile.h>
#include <qlist.h>
#include <qstring.h>
#ifndef BUILD_QSCXMLC
#include "qscxmlinvokableservice_p.h"
#include "qscxmldatamodel_p.h"
#include "qscxmlstatemachine_p.h"
#include "qscxmlstatemachine.h"
#include "qscxmltabledata_p.h"
#include <private/qmetaobjectbuilder_p.h>
#endif
#include <QtCore/qmap.h>
#include <functional>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtscxml/src/scxml/qscxmlcompiler.cpp, line 1144, as _ZN13DocumentModel4NodeD2Ev
inline DocumentModel::Node::~Node()
{
}

//  from ../qtscxml/src/scxml/qscxmlcompiler.cpp, line 1266, as _ZN13DocumentModel5Scxml6acceptEPNS_11NodeVisitorE
inline void DocumentModel::Scxml::accept(DocumentModel::NodeVisitor *visitor)
{
    if (visitor->visit(this)) {
        visitor->visit(children);
        visitor->visit(dataElements);
        if (script)
            script->accept(visitor);
        visitor->visit(&initialSetup);
    }
    visitor->endVisit(this);
}
//  -----------------------------------------------------------------------

//  A DocumentModel::Scxml that Python can take functions over in. Every DocumentModel::Scxml
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteDocumentModel_ScxmlCall0)(const void *, DocumentModel::StateOrTransition *, int *);
typedef void * (*CuteDocumentModel_ScxmlCall1)(const void *, int *);
typedef void (*CuteDocumentModel_ScxmlCall2)(const void *, DocumentModel::NodeVisitor *, int *);
typedef void * (*CuteDocumentModel_ScxmlCall3)(const void *, int *);
typedef void * (*CuteDocumentModel_ScxmlCall4)(const void *, int *);
typedef void * (*CuteDocumentModel_ScxmlCall5)(const void *, int *);
typedef void * (*CuteDocumentModel_ScxmlCall6)(const void *, int *);
typedef void * (*CuteDocumentModel_ScxmlCall7)(const void *, int *);
typedef void * (*CuteDocumentModel_ScxmlCall8)(const void *, int *);
typedef void * (*CuteDocumentModel_ScxmlCall9)(const void *, int *);
typedef void * (*CuteDocumentModel_ScxmlCall10)(const void *, int *);
class CuteDocumentModel_Scxml : public DocumentModel::Scxml {
public:
  using DocumentModel::Scxml::Scxml;
  void *taken[11] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN13DocumentModel14StateContainer3addEPNS_17StateOrTransitionE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel4Node7asScxmlEv")) {
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
    if (!std::strcmp(key, "_ZN13DocumentModel4Node4asIfEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel4Node6asSendEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel4Node8asInvokeEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel4Node8asScriptEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel4Node12asTransitionEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN13DocumentModel4Node14asHistoryStateEv")) {
      taken[10] = call;
      return true;
    }
    return false;
  }

  //  void DocumentModel::Scxml::add(StateOrTransition *s)
  void add(DocumentModel::StateOrTransition *s) override {
    if (taken[0]) {
      int handled = 0;
      CuteDocumentModel_ScxmlCall0 call = reinterpret_cast<CuteDocumentModel_ScxmlCall0>(taken[0]);
      call(this, s, &handled);
      if (handled) return;
    }
    DocumentModel::Scxml::add(s);
  }

  //  Scxml *DocumentModel::Scxml::asScxml()
  DocumentModel::Scxml *asScxml() override {
    if (taken[1]) {
      int handled = 0;
      CuteDocumentModel_ScxmlCall1 call = reinterpret_cast<CuteDocumentModel_ScxmlCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::Scxml *>(given);
    }
    return DocumentModel::Scxml::asScxml();
  }

  //  void DocumentModel::Scxml::accept(NodeVisitor *visitor)
  void accept(DocumentModel::NodeVisitor *visitor) override {
    if (taken[2]) {
      int handled = 0;
      CuteDocumentModel_ScxmlCall2 call = reinterpret_cast<CuteDocumentModel_ScxmlCall2>(taken[2]);
      call(this, visitor, &handled);
      if (handled) return;
    }
    DocumentModel::Scxml::accept(visitor);
  }

  //  AbstractState *DocumentModel::StateContainer::asAbstractState()
  DocumentModel::AbstractState *asAbstractState() override {
    if (taken[3]) {
      int handled = 0;
      CuteDocumentModel_ScxmlCall3 call = reinterpret_cast<CuteDocumentModel_ScxmlCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::AbstractState *>(given);
    }
    return DocumentModel::StateContainer::asAbstractState();
  }

  //  State *DocumentModel::StateContainer::asState()
  DocumentModel::State *asState() override {
    if (taken[4]) {
      int handled = 0;
      CuteDocumentModel_ScxmlCall4 call = reinterpret_cast<CuteDocumentModel_ScxmlCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::State *>(given);
    }
    return DocumentModel::StateContainer::asState();
  }

  //  If *DocumentModel::Node::asIf()
  DocumentModel::If *asIf() override {
    if (taken[5]) {
      int handled = 0;
      CuteDocumentModel_ScxmlCall5 call = reinterpret_cast<CuteDocumentModel_ScxmlCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::If *>(given);
    }
    return DocumentModel::Node::asIf();
  }

  //  Send *DocumentModel::Node::asSend()
  DocumentModel::Send *asSend() override {
    if (taken[6]) {
      int handled = 0;
      CuteDocumentModel_ScxmlCall6 call = reinterpret_cast<CuteDocumentModel_ScxmlCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::Send *>(given);
    }
    return DocumentModel::Node::asSend();
  }

  //  Invoke *DocumentModel::Node::asInvoke()
  DocumentModel::Invoke *asInvoke() override {
    if (taken[7]) {
      int handled = 0;
      CuteDocumentModel_ScxmlCall7 call = reinterpret_cast<CuteDocumentModel_ScxmlCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::Invoke *>(given);
    }
    return DocumentModel::Node::asInvoke();
  }

  //  Script *DocumentModel::Node::asScript()
  DocumentModel::Script *asScript() override {
    if (taken[8]) {
      int handled = 0;
      CuteDocumentModel_ScxmlCall8 call = reinterpret_cast<CuteDocumentModel_ScxmlCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::Script *>(given);
    }
    return DocumentModel::Node::asScript();
  }

  //  Transition *DocumentModel::Node::asTransition()
  DocumentModel::Transition *asTransition() override {
    if (taken[9]) {
      int handled = 0;
      CuteDocumentModel_ScxmlCall9 call = reinterpret_cast<CuteDocumentModel_ScxmlCall9>(taken[9]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::Transition *>(given);
    }
    return DocumentModel::Node::asTransition();
  }

  //  HistoryState *DocumentModel::Node::asHistoryState()
  DocumentModel::HistoryState *asHistoryState() override {
    if (taken[10]) {
      int handled = 0;
      CuteDocumentModel_ScxmlCall10 call = reinterpret_cast<CuteDocumentModel_ScxmlCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<DocumentModel::HistoryState *>(given);
    }
    return DocumentModel::Node::asHistoryState();
  }
};

//  DocumentModel::Scxml::Scxml(const XmlLocation &xmlLocation)
extern "C" Q_DECL_EXPORT
DocumentModel::Scxml *ritual_ZN13DocumentModel5ScxmlC1ERKNS_11XmlLocationE(
    const DocumentModel::XmlLocation *xmlLocation) {
  return new CuteDocumentModel_Scxml(*xmlLocation);
}

//  void DocumentModel::Scxml::add(StateOrTransition *s)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DocumentModel5Scxml3addEPNS_17StateOrTransitionE(
    DocumentModel::Scxml *self,
    DocumentModel::StateOrTransition *s) {
  self->add(s);
}

//  Scxml *DocumentModel::Scxml::asScxml()
extern "C" Q_DECL_EXPORT
DocumentModel::Scxml *ritual_ZN13DocumentModel5Scxml7asScxmlEv(
    DocumentModel::Scxml *self) {
  return self->asScxml();
}

//  void DocumentModel::Scxml::accept(NodeVisitor *visitor)
extern "C" Q_DECL_EXPORT
void ritual_ZN13DocumentModel5Scxml6acceptEPNS_11NodeVisitorE(
    DocumentModel::Scxml *self,
    DocumentModel::NodeVisitor *visitor) {
  self->accept(visitor);
}

//  DocumentModel::Scxml as the DocumentModel::Node it is built on
extern "C" Q_DECL_EXPORT
DocumentModel::Node *ritual_cast_DocumentModel_Scxml_DocumentModel_Node(
    DocumentModel::Scxml *self) {
  return static_cast<DocumentModel::Node *>(self);
}

//  a Python function taken by a CuteDocumentModel_Scxml, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_DocumentModel_Scxml(
    DocumentModel::Scxml *self,
    const char *key,
    void *call) {
  return static_cast<CuteDocumentModel_Scxml *>(self)->take(key, call);
}

//  void DocumentModel::Scxml::add(StateOrTransition *s)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13DocumentModel5Scxml3addEPNS_17StateOrTransitionE(
    DocumentModel::Scxml *self,
    DocumentModel::StateOrTransition *s) {
  self->DocumentModel::Scxml::add(s);
}

//  Scxml *DocumentModel::Scxml::asScxml()
extern "C" Q_DECL_EXPORT
DocumentModel::Scxml *ritual_own_ZN13DocumentModel5Scxml7asScxmlEv(
    DocumentModel::Scxml *self) {
  return self->DocumentModel::Scxml::asScxml();
}

//  void DocumentModel::Scxml::accept(NodeVisitor *visitor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13DocumentModel5Scxml6acceptEPNS_11NodeVisitorE(
    DocumentModel::Scxml *self,
    DocumentModel::NodeVisitor *visitor) {
  self->DocumentModel::Scxml::accept(visitor);
}
